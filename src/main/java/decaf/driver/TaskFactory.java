package decaf.driver;

import decaf.frontend.parsing.JaccParser;
import decaf.frontend.tree.Tree;
import decaf.frontend.typecheck.Namer;
import decaf.frontend.typecheck.Typer;

import java.io.InputStream;

/**
 * Supported tasks of Decaf compiler.
 */
public class TaskFactory {
    private final Config config;

    public TaskFactory(Config config) {
        this.config = config;
    }

    public Task<InputStream, Tree.TopLevel> parse() {
        return new JaccParser(config);
    }

    public Task<InputStream, Tree.TopLevel> typeCheck() {
        return parse().then(new Namer(config)).then(new Typer(config));
    }
//
//    public Task<InputStream, TacProg> tacGen() {
//        return typeCheck().then(new TacGen(config));
//    }
//
//    public Task<InputStream, TacProg> optimize() {
//        return tacGen().then(new Optimizer(config));
//    }
//
//    public Task<InputStream, String> mips() {
//        var emitter = new MipsAsmEmitter();
//        return tacGen().then(new Asm(emitter, new BruteRegAlloc(emitter), config));
//    }
}
