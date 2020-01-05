package decaf.backend.opt;

import decaf.backend.dataflow.CFG;
import decaf.backend.dataflow.CFGBuilder;
import decaf.backend.dataflow.LivenessAnalyzer;
import decaf.backend.dataflow.Loc;
import decaf.driver.Config;
import decaf.driver.Phase;
import decaf.lowlevel.instr.Temp;
import decaf.lowlevel.tac.Simulator;
import decaf.lowlevel.tac.TacInstr;
import decaf.lowlevel.tac.TacProg;

import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * TAC optimization phase: optimize a TAC program.
 * <p>
 * The original decaf compiler has NO optimization, thus, we implement the transformation as identity function.
 */
public class Optimizer extends Phase<TacProg, TacProg> {
    public Optimizer(Config config) {
        super("optimizer", config);
    }

    @Override
    public TacProg transform(TacProg input) {
        var analyzer = new LivenessAnalyzer<TacInstr>();
        CFG<TacInstr> cfg = null;
        for (var func : input.funcs){
            var seqs = func.getInstrSeq();
            boolean change = false;
            do {
                var builder = new CFGBuilder<TacInstr>();
                cfg = builder.buildFrom(seqs);
                analyzer.accept(cfg);
                change = false;
                for (var node : cfg.nodes) {
                    var it = node.backwardIterator();
                    Loc<TacInstr> changedLoc = null;
                    while (it.hasNext()) {
                        var loc = it.next();
                        Temp dst = null;
                        if (changedLoc != null) {
                            loc.liveOut = changedLoc.liveOut;
                            changedLoc = null;
                        }
                        if (loc.instr.dsts.length > 0 && !loc.liveOut.contains(loc.instr.dsts[0])) {
                            if (loc.instr instanceof TacInstr.DirectCall) {
                                var entry = ((TacInstr.DirectCall)loc.instr).entry;
                                var instr = new TacInstr.DirectCall(entry);
                                func.replace(loc.instr, instr);
                            } else if (loc.instr instanceof TacInstr.IndirectCall) {
                                var entry = ((TacInstr.IndirectCall)loc.instr).entry;
                                var instr = new TacInstr.IndirectCall(entry);
                                func.replace(loc.instr, instr);
                            } else {
                                func.remove(loc.instr);
                                change = true;
                                changedLoc = loc;
                            }
                        }
                    }
                    if (change) break;
                }
            }while(change);
        }
        return input;
    }

    @Override
    public void onSucceed(TacProg program) {
        if (config.target.equals(Config.Target.PA4)) {
            // First dump the tac program to file,
            var path = config.dstPath.resolve(config.getSourceBaseName() + ".tac");
            try {
                var printer = new PrintWriter(path.toFile());
                program.printTo(printer);
                printer.close();
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }

            // and then execute it using our simulator.
            var simulator = new Simulator(System.in, config.output);
            simulator.execute(program);
        }
    }
}
