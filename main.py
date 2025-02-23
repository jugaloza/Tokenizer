from regex import RegexTokenizer
from basic import BasicTokenizer

text = """As we saw in Chapter 2, “The Yocto Project,” the script oe-init-build-env
creates and initializes the build environment. This script is one of the scripts contained
within the build system. A build system and build environments form a 1:n relationship: a
build system can be associated with any number of build environments, but a build
environment can be associated with only one build system. This is an important limitation
you need to be aware of when you are using more than one Yocto Project release at a time.
You can use a build environment only with the version of the build system it was
originally created with. Using a build system to initialize a build environment that is
different from the one originally used to create the build environment leads to build
failures.A build system always has to include metadata layers, which provide recipes and
configuration files. When you create a build environment with the oe-init-build-
env script of the build system, the script automatically sets up a
conf/bblayers.conf file that includes the three base layers: meta, meta-yocto-
bsp, and meta-yocto. These base layers are sufficient to build the standard Poky
reference distribution. However, as an embedded Linux developer, you eventually want to
create your own distribution, add your own software packages, and potentially provide
your own BSP for your target hardware. This goal is accomplished by including other
metadata layers with the build system.
In the following section, we explore the structures of the build system, the build
environment, and the metadata layers in more detail.
"""

if __name__ == "__main__":
    #ids = encode_text(text)
    #print(get_stats(ids))
    #print(decode_text(ids))
    tokenizer = BasicTokenizer()

    tokenizer.train(text, vocab_size=512)
    input_text = """In the following section, we explore the structures of the build system, the build
environment, and the metadata layers in more detail."""
    encoded_text = tokenizer.encode(input_text)
    print(f"encoded text: {encoded_text}")
    decoded_text = tokenizer.decode(encoded_text)

    print(f"decoded text : {decoded_text}")
    #print(tokenizer.merges)
    #print(tokenizer.vocab.keys())