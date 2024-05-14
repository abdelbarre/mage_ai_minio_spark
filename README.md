![](https://cdn-images-1.medium.com/max/1200/1*FO9f5aVy0mb5VYJwxrv3YQ.png)

In this data engineering post, we'll explore cutting-edge open-source technologies that can assist us in constructing a resilient data engineering pipeline. If you're interested in learning more about Mage AI, please refer to this article. To begin with Mage AI,

> you can read my first article about mage Ai at [link](https://medium.com/towardsdev/etl-mage-the-airflow-replacement-06f46c567248).

Let's kick things off with a quick overview of the technologies that will be utilized in this demonstration.

#### Spark :
Apache Spark is an open-source distributed computing system that is designed for big data processing and analytics. It provides an easy-to-use and unified platform for batch processing, real-time processing, machine learning, and interactive analytics.
#### Delta lake :
Delta Lake is an open-source storage layer that brings reliability to data lakes. It provides ACID transactions, scalable metadata handling, and unifies streaming and batch data processing. Delta Lake runs on top of existing data lake solutions such as Apache Spark and Hadoop Distributed File System (HDFS) and extends their capabilities to handle big data use cases more effectively.
#### Mage Ai :
Mage is an open-source, hybrid framework for transforming and integrating data
![mage AI](https://cdn-images-1.medium.com/max/800/0*GRwkLSdVPnAG75l5.png)

#### Minio :
MinIO is an open-source, distributed object storage system. It is designed to be highly scalable and can be deployed on-premises, in the cloud, or in a hybrid environment. MinIO is compatible with Amazon S3 API, allowing applications that work with S3 to seamlessly switch to MinIO without any code changes.
![minio](https://cdn-images-1.medium.com/max/800/1*kYzDDtmAonxGhmoEhnjz7g.png)

Here are some key features of MinIO:

- High Performance: MinIO is optimized for high performance and low latency, making it suitable for use cases that require rapid access to large amounts of data.
- Scalability: MinIO is designed to scale horizontally, allowing you to add more storage nodes as your data needs grow. It uses a distributed architecture to distribute data across multiple servers, ensuring high availability and fault tolerance.
- Data Protection: MinIO provides features such as data encryption, access control, and versioning to protect your data from unauthorized access, tampering, and data loss.
- S3 Compatibility: MinIO is fully compatible with the Amazon S3 API, which means that you can use existing S3-compatible tools and libraries with MinIO without any modifications.
- Ease of Use: MinIO is easy to deploy and manage, with a simple command-line interface and web-based dashboard for monitoring and administration.
- Use Cases: MinIO is suitable for a wide range of use cases, including data storage, backup and archiving, content distribution, data lakes, and cloud-native applications

## 1 - installation and configuration
![](https://cdn-images-1.medium.com/max/800/1*4qlL1JEx6kNROGVk_uKYFw.gif)

We will use docker as containerization tool for many reasons :

- Simplifies software development by providing a consistent and isolated environment.
- Enhances interoperability by enabling applications to be easily deployed on various platforms without compatibility issues.
- Speeds up the development process by eliminating the need to set up complex development environments manually.
- Improves scalability and flexibility as Docker containers can be quickly deployed and scaled up or down as needed.

The following code is for docker compose file

```yaml
version: '3'
services:
  mageai:
    container_name: mage_spark_test
    build:
      context: https://github.com/mage-ai/compose-quickstart.git
      dockerfile: Dockerfile
    environment:
      - MINIO_URL=http://minio:9000
    ports:
      - '6789:6789'
    command: >
      bash -c "
      echo 'deb http://deb.debian.org/debian bullseye main' > /etc/apt/sources.list.d/bullseye.list &&
      apt-get update -y &&
      apt-get install -y openjdk-11-jdk &&
      rm /etc/apt/sources.list.d/bullseye.list &&
      pip install pyspark &&
      pip install delta-spark &&
      pip install minio &&
      /app/run_app.sh mage start demo_project
      "

  minio:
    container_name: spark-minio-mage
    image: quay.io/minio/minio
    ports:
      - '9000:9000'
      - '9001:9001'
    volumes:
      - './minio_data:/data'
    environment:
      - MINIO_ROOT_USER=admin
      - MINIO_ROOT_PASSWORD=admin123456789
      - MINIO_DEFAULT_BUCKETS=your_bucket_name
    command: server --console-address ":9001" /data

```