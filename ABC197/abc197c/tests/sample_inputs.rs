use cli_test_dir::*;

const BIN: &'static str = "./main";

#[test]
fn sample1() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(r#"4
1 1
2 2        
"#)
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "2.00000000000 1.00000000000\n");
    assert!(output.stderr_str().is_empty());
}

#[test]
fn sample2() {
    let testdir = TestDir::new(BIN, "");
    let output = testdir
        .cmd()
        .output_with_stdin(r#"6
5 3
7 4        
"#)
        .tee_output()
        .expect_success();
    assert_eq!(output.stdout_str(), "5.93301270189 2.38397459622\n");
    assert!(output.stderr_str().is_empty());
}