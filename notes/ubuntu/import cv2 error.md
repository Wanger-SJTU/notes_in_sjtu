> ```
> import cv2
> 
> ImportError: dynamic module does not define module export function (PyInit_cv2)
> ```



**PROBLEM:** The reason this was happening was that I had set the PYTHONPATH variable on Ubuntu for some other software in the past. The way Anaconda environments work is that they hard link everything that is installed into the environment. Thus each environment is a completely separate installation of Python and all the packages. By using hard links, this is done efficiently. Thus, there's no need to mess with PYTHONPATH because the Python binary in the environment already searches the site-packages in the environment, and the lib of the environment, and so on.

By setting the PYTHONPATH environment variable we interfere with Anaconda's natural behavior thus forcing it to look for libraries in the paths defined by the PYTHONPATH which is generally set to your local machine paths and not the environment paths.

**SOLUTION:** Best thing to do would be to go to your `.bashrc` file and comment/remove the lines that set a `PYTHONPATH`. However, if you don't want to do that you can always do `"unset PYTHONPATH"` before activating an environment and everything will work like a charm.

---

 solution from:

https://github.com/udacity/CarND-Term1-Starter-Kit-Test/issues/3