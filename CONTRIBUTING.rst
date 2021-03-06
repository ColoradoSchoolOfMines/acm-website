Contributing to this Project
============================

Contributions are welcome... please fork and submit a pull request! If you are
a member of our ACM Chapter, you should be able to work out of this repository
(see below, you will still need to make a branch and submit a PR for most
changes).

.. sidebar:: About This File

   This is a "how to contribute" file, not a "requirements for contributions"
   file. Chances are, your code will undergo a code review and might receive
   constructive criticism on nit-picky things. **Don't take a code review
   personally; the point of the review process is to make sure the code for the
   site stays clean and bug free.** Things that are not "small nit-picky"
   things (i.e., they would cause a major rework before you start working on a
   contribution) should be added to this file.

Coding Style
------------

`PEP-8`_ is to be followed **strictly**; however line lengths of up to 90 or
100 columns is OK if the purpose of the line is still cleanly conveyed.

.. _`PEP-8`: https://www.python.org/dev/peps/pep-0008/

This is a Python project, and hence documentation should be in reStructuredText
format.

Markup languages (XHTML, CSS) should use 2 spaces for indentation.

Other Notes
-----------

* Keep use of JavaScripts to a minimum. If you need to use JavaScripts, all
  features of the site should still work with JavaScripts disabled (and the
  interface to do so should not have anything broken that is confusing).
* Don't use "auto PEP-8" tools. There is more than one way to PEP-8; the
  guidelines define a constraint set with more than one solution. It is best
  left to the programmer to find a clean way to write their code within that
  constraint set.
* You are welcome to rebase on your own local clone of this repository;
  however, once changes have been pushed to this remote, rebasing must be kept
  to an absolute minimum (even "on your own branch"). If you wish to rebase
  commits which have already been pushed, you must contact Jack and ask for
  permission before doing a force push.
* Major changes to the site must be developed in their own branch, then submit
  a PR. If you have quick-fixes, pushing to ``master`` is OK.
* Jack will not pull the ``master`` branch to the production site if he tests
  it and discovers software bugs or regressions. Therefore, try to keep
  ``master`` fairly bug-free so that we can pull as often as we need.
* If you assign a task to someone, but then you later decide that you want to
  do it yourself, contact that person first to prevent duplicated work.
* Don't assume any contributing guidelines this file does not state.

