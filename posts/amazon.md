I recently got a $100 credit for Amazon AWS, and I've been trying different things, notably:

- **Litecoin mining on a GPU instance**: couldn't get it to work, CUDA graphic cards suck for mining (although are really good for other things apart of gaming)

- **Just trying out other AWS services**: I now use Route 53 as my DNS provider, EC2 for my [Dokku](https://github.com/progrium/dokku) instance (just a t1.micro though) and S3 for servig static assets for my sites (they're all now updated for it).

Amazon got it right with AWS, and is such a nice service where I can keep my ISP needs centralized in the same place, and now since AWS dashboard has been updated, is even nicer.

![AWS Services](https://pablo-assets.s3.amazonaws.com/etc/awsservices.png)

But **S3** is what I actually love. It's **fast as hell**, and actually really simple yet useful (and cheap!). You just create a bucket and push files. The image I put here now just takes around 150 ms to download. Well you can't really see the improvement though, but it's really fast.

Also there's something else which I like, and that's **Route 53**. I was tired of FreeDNS and Cloudflare, so I remembered Amazon offered a DNS hosting service too, so I just went there. Works really good, it's cheap as well, and simple to use.

Also, just to talk about the last service I actually use, **EC2**, is just a classic. Virtual instances that can suit anyone's needs. They have general use instances with a range of CPU cores and RAM amount, to high end memory instances with 244GB of RAM, going through GPU (instances with a GRID K520 card) and disk instances (nearly 50TB of storage).

Amazon got also a lot of other services which can as well, suit anyone needs. Databases, search engines, private clouds, CDNs, analytics,... Basically, a bunch of things for almost anything in the web world.




