# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBucketRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "CreateBucketRequest"

    sensitive_list = []

    openapi_types = {
        'bucket_name': 'str',
        'date': 'str',
        'x_obs_acl': 'str',
        'x_obs_storage_class': 'str',
        'x_obs_grant_read': 'str',
        'x_obs_grant_write': 'str',
        'x_obs_grant_read_acp': 'str',
        'x_obs_grant_write_acp': 'str',
        'x_obs_grant_full_control': 'str',
        'x_obs_grant_read_delivered': 'str',
        'x_obs_grant_full_control_delivered': 'str',
        'x_obs_az_redundancy': 'str',
        'x_obs_fs_file_interface': 'str',
        'x_obs_epid': 'str',
        'x_obs_cluster_type': 'str',
        'x_obs_location_clustergroup_id': 'str',
        'x_obs_ies_location': 'str',
        'body': 'CreateBucketRequestBody'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'date': 'Date',
        'x_obs_acl': 'x-obs-acl',
        'x_obs_storage_class': 'x-obs-storage-class',
        'x_obs_grant_read': 'x-obs-grant-read',
        'x_obs_grant_write': 'x-obs-grant-write',
        'x_obs_grant_read_acp': 'x-obs-grant-read-acp',
        'x_obs_grant_write_acp': 'x-obs-grant-write-acp',
        'x_obs_grant_full_control': 'x-obs-grant-full-control',
        'x_obs_grant_read_delivered': 'x-obs-grant-read-delivered',
        'x_obs_grant_full_control_delivered': 'x-obs-grant-full-control-delivered',
        'x_obs_az_redundancy': 'x-obs-az-redundancy',
        'x_obs_fs_file_interface': 'x-obs-fs-file-interface',
        'x_obs_epid': 'x-obs-epid',
        'x_obs_cluster_type': 'x-obs-cluster-type',
        'x_obs_location_clustergroup_id': 'x-obs-location-clustergroup-id',
        'x_obs_ies_location': 'x-obs-ies-location',
        'body': 'body'
    }

    def __init__(self, bucket_name=None, date=None, x_obs_acl=None, x_obs_storage_class=None, x_obs_grant_read=None, x_obs_grant_write=None, x_obs_grant_read_acp=None, x_obs_grant_write_acp=None, x_obs_grant_full_control=None, x_obs_grant_read_delivered=None, x_obs_grant_full_control_delivered=None, x_obs_az_redundancy=None, x_obs_fs_file_interface=None, x_obs_epid=None, x_obs_cluster_type=None, x_obs_location_clustergroup_id=None, x_obs_ies_location=None, body=None):
        """CreateBucketRequest

        The model defined in huaweicloud sdk

        :param bucket_name: 考虑到桶名会作为访问域名的一部分，需要参与域名解析，因此桶名需要满足DNS域名规范。OBS系统在接受创桶请求时，会对桶名进行严格的检查，具体规则如下： 需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。用户删除桶后，立即创建同名桶或并行文件系统会创建失败，需要等待30分钟才能创建。 长度范围为3到63个字符，支持小写字母、数字、中划线（-）、英文句号（.）。 禁止两个英文句号（.）相邻，禁止英文句号（.）和中划线（-）相邻，禁止以英文句号（.）和中划线（-）开头或结尾。 禁止使用IP地址。 须知： 当使用HTTPS协议访问OBS系统时，由于SSL的通配符证书仅匹配不包含\&quot;.\&quot;的桶。这将导致桶名包含\&quot;.\&quot;的桶在访问OBS系统时，客户端会提示证书校验存在风险，比如浏览器安全提示会呈现红色告警。因此如非必要，请尽量不要在桶名中包含\&quot;.\&quot;。 
        :type bucket_name: str
        :param date: 请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 
        :type date: str
        :param x_obs_acl: 创建桶时，可以加上此消息头设置桶的权限控制策略，使用的策略为预定义的常用策略，包括：private、public-read、public-read-write、public-read-delivered、public-read-write-delivered、bucket-owner-full-control（各策略详细说明见ACL章节的“使用头域设置ACL”）。 
        :type x_obs_acl: str
        :param x_obs_storage_class: 创建桶时，可以加上此消息头设置桶的默认存储类型，默认存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）、HIGH_PERFORMANCE（高性能存储，只有并行文件系统支持）。如果没有指定此头域，则创建的桶为标准存储类型。 
        :type x_obs_storage_class: str
        :param x_obs_grant_read: 授权给指定domain下的所有用户有READ权限。允许列举桶内对象、列举桶中多段任务、列举桶中多版本对象、获取桶元数据。 
        :type x_obs_grant_read: str
        :param x_obs_grant_write: 授权给指定domain下的所有用户有WRITE权限。允许创建、删除、覆盖桶内所有对象，允许初始化段、上传段、拷贝段、合并段、取消多段上传任务。 
        :type x_obs_grant_write: str
        :param x_obs_grant_read_acp: 授权给指定domain下的所有用户有READ_ACP权限。允许读桶的ACL信息。 
        :type x_obs_grant_read_acp: str
        :param x_obs_grant_write_acp: 授权给指定domain下的所有用户有WRITE_ACP权限，允许修改桶的ACL信息。 
        :type x_obs_grant_write_acp: str
        :param x_obs_grant_full_control: 授权给指定domain下的所有用户有FULL_CONTROL权限。 
        :type x_obs_grant_full_control: str
        :param x_obs_grant_read_delivered: 授权给指定domain下的所有用户有READ权限，并且在默认情况下，该READ权限将传递给桶内所有对象。 
        :type x_obs_grant_read_delivered: str
        :param x_obs_grant_full_control_delivered: 授权给指定domain下的所有用户有FULL_CONTROL权限，并且在默认情况下，该FULL_CONTROL权限将传递给桶内所有对象。 
        :type x_obs_grant_full_control_delivered: str
        :param x_obs_az_redundancy: 创建桶时带上此消息头设置桶的存储类型为多AZ。不携带时默认为单AZ。用户携带该头域指定新创的桶的存储类型为多AZ，存在一种情况是当该区域如果不支持多AZ存储，则该桶的存储类型仍为单AZ。 
        :type x_obs_az_redundancy: str
        :param x_obs_fs_file_interface: 创建桶时可以带上此消息头以创建并行文件系统。 
        :type x_obs_fs_file_interface: str
        :param x_obs_epid: 企业项目id，开通企业项目的用户可以从企业项目服务获取，格式为uuid，默认项目传“0”或者不带该头域，未开通企业项目的用户可以不带该头域。 
        :type x_obs_epid: str
        :param x_obs_cluster_type: 指定桶是创建在公共集群还是专属集群。 
        :type x_obs_cluster_type: str
        :param x_obs_location_clustergroup_id: 集群显性化创桶时，指定的集群组ID 
        :type x_obs_location_clustergroup_id: str
        :param x_obs_ies_location: 如果是要创建在IES站点上，则指定IES站点的AZ ID。此参数和x-obs-cluster-type不可共存。 
        :type x_obs_ies_location: str
        :param body: Body of the CreateBucketRequest
        :type body: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        
        

        self._bucket_name = None
        self._date = None
        self._x_obs_acl = None
        self._x_obs_storage_class = None
        self._x_obs_grant_read = None
        self._x_obs_grant_write = None
        self._x_obs_grant_read_acp = None
        self._x_obs_grant_write_acp = None
        self._x_obs_grant_full_control = None
        self._x_obs_grant_read_delivered = None
        self._x_obs_grant_full_control_delivered = None
        self._x_obs_az_redundancy = None
        self._x_obs_fs_file_interface = None
        self._x_obs_epid = None
        self._x_obs_cluster_type = None
        self._x_obs_location_clustergroup_id = None
        self._x_obs_ies_location = None
        self._body = None
        self.discriminator = None

        self.bucket_name = bucket_name
        if date is not None:
            self.date = date
        if x_obs_acl is not None:
            self.x_obs_acl = x_obs_acl
        if x_obs_storage_class is not None:
            self.x_obs_storage_class = x_obs_storage_class
        if x_obs_grant_read is not None:
            self.x_obs_grant_read = x_obs_grant_read
        if x_obs_grant_write is not None:
            self.x_obs_grant_write = x_obs_grant_write
        if x_obs_grant_read_acp is not None:
            self.x_obs_grant_read_acp = x_obs_grant_read_acp
        if x_obs_grant_write_acp is not None:
            self.x_obs_grant_write_acp = x_obs_grant_write_acp
        if x_obs_grant_full_control is not None:
            self.x_obs_grant_full_control = x_obs_grant_full_control
        if x_obs_grant_read_delivered is not None:
            self.x_obs_grant_read_delivered = x_obs_grant_read_delivered
        if x_obs_grant_full_control_delivered is not None:
            self.x_obs_grant_full_control_delivered = x_obs_grant_full_control_delivered
        if x_obs_az_redundancy is not None:
            self.x_obs_az_redundancy = x_obs_az_redundancy
        if x_obs_fs_file_interface is not None:
            self.x_obs_fs_file_interface = x_obs_fs_file_interface
        if x_obs_epid is not None:
            self.x_obs_epid = x_obs_epid
        if x_obs_cluster_type is not None:
            self.x_obs_cluster_type = x_obs_cluster_type
        if x_obs_location_clustergroup_id is not None:
            self.x_obs_location_clustergroup_id = x_obs_location_clustergroup_id
        if x_obs_ies_location is not None:
            self.x_obs_ies_location = x_obs_ies_location
        if body is not None:
            self.body = body

    @property
    def bucket_name(self):
        """Gets the bucket_name of this CreateBucketRequest.

        考虑到桶名会作为访问域名的一部分，需要参与域名解析，因此桶名需要满足DNS域名规范。OBS系统在接受创桶请求时，会对桶名进行严格的检查，具体规则如下： 需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。用户删除桶后，立即创建同名桶或并行文件系统会创建失败，需要等待30分钟才能创建。 长度范围为3到63个字符，支持小写字母、数字、中划线（-）、英文句号（.）。 禁止两个英文句号（.）相邻，禁止英文句号（.）和中划线（-）相邻，禁止以英文句号（.）和中划线（-）开头或结尾。 禁止使用IP地址。 须知： 当使用HTTPS协议访问OBS系统时，由于SSL的通配符证书仅匹配不包含\".\"的桶。这将导致桶名包含\".\"的桶在访问OBS系统时，客户端会提示证书校验存在风险，比如浏览器安全提示会呈现红色告警。因此如非必要，请尽量不要在桶名中包含\".\"。 

        :return: The bucket_name of this CreateBucketRequest.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this CreateBucketRequest.

        考虑到桶名会作为访问域名的一部分，需要参与域名解析，因此桶名需要满足DNS域名规范。OBS系统在接受创桶请求时，会对桶名进行严格的检查，具体规则如下： 需全局唯一，不能与已有的任何桶名称重复，包括其他用户创建的桶。用户删除桶后，立即创建同名桶或并行文件系统会创建失败，需要等待30分钟才能创建。 长度范围为3到63个字符，支持小写字母、数字、中划线（-）、英文句号（.）。 禁止两个英文句号（.）相邻，禁止英文句号（.）和中划线（-）相邻，禁止以英文句号（.）和中划线（-）开头或结尾。 禁止使用IP地址。 须知： 当使用HTTPS协议访问OBS系统时，由于SSL的通配符证书仅匹配不包含\".\"的桶。这将导致桶名包含\".\"的桶在访问OBS系统时，客户端会提示证书校验存在风险，比如浏览器安全提示会呈现红色告警。因此如非必要，请尽量不要在桶名中包含\".\"。 

        :param bucket_name: The bucket_name of this CreateBucketRequest.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def date(self):
        """Gets the date of this CreateBucketRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :return: The date of this CreateBucketRequest.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this CreateBucketRequest.

        请求发起端的日期和时间，例如：Wed, 27 Jun 2018 13:39:15 +0000。 默认值：无。 条件：如果消息头中带了x-obs-date字段，则可以不带该字段，其他情况下必选。 

        :param date: The date of this CreateBucketRequest.
        :type date: str
        """
        self._date = date

    @property
    def x_obs_acl(self):
        """Gets the x_obs_acl of this CreateBucketRequest.

        创建桶时，可以加上此消息头设置桶的权限控制策略，使用的策略为预定义的常用策略，包括：private、public-read、public-read-write、public-read-delivered、public-read-write-delivered、bucket-owner-full-control（各策略详细说明见ACL章节的“使用头域设置ACL”）。 

        :return: The x_obs_acl of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_acl

    @x_obs_acl.setter
    def x_obs_acl(self, x_obs_acl):
        """Sets the x_obs_acl of this CreateBucketRequest.

        创建桶时，可以加上此消息头设置桶的权限控制策略，使用的策略为预定义的常用策略，包括：private、public-read、public-read-write、public-read-delivered、public-read-write-delivered、bucket-owner-full-control（各策略详细说明见ACL章节的“使用头域设置ACL”）。 

        :param x_obs_acl: The x_obs_acl of this CreateBucketRequest.
        :type x_obs_acl: str
        """
        self._x_obs_acl = x_obs_acl

    @property
    def x_obs_storage_class(self):
        """Gets the x_obs_storage_class of this CreateBucketRequest.

        创建桶时，可以加上此消息头设置桶的默认存储类型，默认存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）、HIGH_PERFORMANCE（高性能存储，只有并行文件系统支持）。如果没有指定此头域，则创建的桶为标准存储类型。 

        :return: The x_obs_storage_class of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_storage_class

    @x_obs_storage_class.setter
    def x_obs_storage_class(self, x_obs_storage_class):
        """Sets the x_obs_storage_class of this CreateBucketRequest.

        创建桶时，可以加上此消息头设置桶的默认存储类型，默认存储类型有3种：STANDARD（标准存储）、WARM（低频访问存储）、COLD（归档存储）、HIGH_PERFORMANCE（高性能存储，只有并行文件系统支持）。如果没有指定此头域，则创建的桶为标准存储类型。 

        :param x_obs_storage_class: The x_obs_storage_class of this CreateBucketRequest.
        :type x_obs_storage_class: str
        """
        self._x_obs_storage_class = x_obs_storage_class

    @property
    def x_obs_grant_read(self):
        """Gets the x_obs_grant_read of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ权限。允许列举桶内对象、列举桶中多段任务、列举桶中多版本对象、获取桶元数据。 

        :return: The x_obs_grant_read of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read

    @x_obs_grant_read.setter
    def x_obs_grant_read(self, x_obs_grant_read):
        """Sets the x_obs_grant_read of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ权限。允许列举桶内对象、列举桶中多段任务、列举桶中多版本对象、获取桶元数据。 

        :param x_obs_grant_read: The x_obs_grant_read of this CreateBucketRequest.
        :type x_obs_grant_read: str
        """
        self._x_obs_grant_read = x_obs_grant_read

    @property
    def x_obs_grant_write(self):
        """Gets the x_obs_grant_write of this CreateBucketRequest.

        授权给指定domain下的所有用户有WRITE权限。允许创建、删除、覆盖桶内所有对象，允许初始化段、上传段、拷贝段、合并段、取消多段上传任务。 

        :return: The x_obs_grant_write of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_write

    @x_obs_grant_write.setter
    def x_obs_grant_write(self, x_obs_grant_write):
        """Sets the x_obs_grant_write of this CreateBucketRequest.

        授权给指定domain下的所有用户有WRITE权限。允许创建、删除、覆盖桶内所有对象，允许初始化段、上传段、拷贝段、合并段、取消多段上传任务。 

        :param x_obs_grant_write: The x_obs_grant_write of this CreateBucketRequest.
        :type x_obs_grant_write: str
        """
        self._x_obs_grant_write = x_obs_grant_write

    @property
    def x_obs_grant_read_acp(self):
        """Gets the x_obs_grant_read_acp of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ_ACP权限。允许读桶的ACL信息。 

        :return: The x_obs_grant_read_acp of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_acp

    @x_obs_grant_read_acp.setter
    def x_obs_grant_read_acp(self, x_obs_grant_read_acp):
        """Sets the x_obs_grant_read_acp of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ_ACP权限。允许读桶的ACL信息。 

        :param x_obs_grant_read_acp: The x_obs_grant_read_acp of this CreateBucketRequest.
        :type x_obs_grant_read_acp: str
        """
        self._x_obs_grant_read_acp = x_obs_grant_read_acp

    @property
    def x_obs_grant_write_acp(self):
        """Gets the x_obs_grant_write_acp of this CreateBucketRequest.

        授权给指定domain下的所有用户有WRITE_ACP权限，允许修改桶的ACL信息。 

        :return: The x_obs_grant_write_acp of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_write_acp

    @x_obs_grant_write_acp.setter
    def x_obs_grant_write_acp(self, x_obs_grant_write_acp):
        """Sets the x_obs_grant_write_acp of this CreateBucketRequest.

        授权给指定domain下的所有用户有WRITE_ACP权限，允许修改桶的ACL信息。 

        :param x_obs_grant_write_acp: The x_obs_grant_write_acp of this CreateBucketRequest.
        :type x_obs_grant_write_acp: str
        """
        self._x_obs_grant_write_acp = x_obs_grant_write_acp

    @property
    def x_obs_grant_full_control(self):
        """Gets the x_obs_grant_full_control of this CreateBucketRequest.

        授权给指定domain下的所有用户有FULL_CONTROL权限。 

        :return: The x_obs_grant_full_control of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control

    @x_obs_grant_full_control.setter
    def x_obs_grant_full_control(self, x_obs_grant_full_control):
        """Sets the x_obs_grant_full_control of this CreateBucketRequest.

        授权给指定domain下的所有用户有FULL_CONTROL权限。 

        :param x_obs_grant_full_control: The x_obs_grant_full_control of this CreateBucketRequest.
        :type x_obs_grant_full_control: str
        """
        self._x_obs_grant_full_control = x_obs_grant_full_control

    @property
    def x_obs_grant_read_delivered(self):
        """Gets the x_obs_grant_read_delivered of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ权限，并且在默认情况下，该READ权限将传递给桶内所有对象。 

        :return: The x_obs_grant_read_delivered of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_read_delivered

    @x_obs_grant_read_delivered.setter
    def x_obs_grant_read_delivered(self, x_obs_grant_read_delivered):
        """Sets the x_obs_grant_read_delivered of this CreateBucketRequest.

        授权给指定domain下的所有用户有READ权限，并且在默认情况下，该READ权限将传递给桶内所有对象。 

        :param x_obs_grant_read_delivered: The x_obs_grant_read_delivered of this CreateBucketRequest.
        :type x_obs_grant_read_delivered: str
        """
        self._x_obs_grant_read_delivered = x_obs_grant_read_delivered

    @property
    def x_obs_grant_full_control_delivered(self):
        """Gets the x_obs_grant_full_control_delivered of this CreateBucketRequest.

        授权给指定domain下的所有用户有FULL_CONTROL权限，并且在默认情况下，该FULL_CONTROL权限将传递给桶内所有对象。 

        :return: The x_obs_grant_full_control_delivered of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_grant_full_control_delivered

    @x_obs_grant_full_control_delivered.setter
    def x_obs_grant_full_control_delivered(self, x_obs_grant_full_control_delivered):
        """Sets the x_obs_grant_full_control_delivered of this CreateBucketRequest.

        授权给指定domain下的所有用户有FULL_CONTROL权限，并且在默认情况下，该FULL_CONTROL权限将传递给桶内所有对象。 

        :param x_obs_grant_full_control_delivered: The x_obs_grant_full_control_delivered of this CreateBucketRequest.
        :type x_obs_grant_full_control_delivered: str
        """
        self._x_obs_grant_full_control_delivered = x_obs_grant_full_control_delivered

    @property
    def x_obs_az_redundancy(self):
        """Gets the x_obs_az_redundancy of this CreateBucketRequest.

        创建桶时带上此消息头设置桶的存储类型为多AZ。不携带时默认为单AZ。用户携带该头域指定新创的桶的存储类型为多AZ，存在一种情况是当该区域如果不支持多AZ存储，则该桶的存储类型仍为单AZ。 

        :return: The x_obs_az_redundancy of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_az_redundancy

    @x_obs_az_redundancy.setter
    def x_obs_az_redundancy(self, x_obs_az_redundancy):
        """Sets the x_obs_az_redundancy of this CreateBucketRequest.

        创建桶时带上此消息头设置桶的存储类型为多AZ。不携带时默认为单AZ。用户携带该头域指定新创的桶的存储类型为多AZ，存在一种情况是当该区域如果不支持多AZ存储，则该桶的存储类型仍为单AZ。 

        :param x_obs_az_redundancy: The x_obs_az_redundancy of this CreateBucketRequest.
        :type x_obs_az_redundancy: str
        """
        self._x_obs_az_redundancy = x_obs_az_redundancy

    @property
    def x_obs_fs_file_interface(self):
        """Gets the x_obs_fs_file_interface of this CreateBucketRequest.

        创建桶时可以带上此消息头以创建并行文件系统。 

        :return: The x_obs_fs_file_interface of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_fs_file_interface

    @x_obs_fs_file_interface.setter
    def x_obs_fs_file_interface(self, x_obs_fs_file_interface):
        """Sets the x_obs_fs_file_interface of this CreateBucketRequest.

        创建桶时可以带上此消息头以创建并行文件系统。 

        :param x_obs_fs_file_interface: The x_obs_fs_file_interface of this CreateBucketRequest.
        :type x_obs_fs_file_interface: str
        """
        self._x_obs_fs_file_interface = x_obs_fs_file_interface

    @property
    def x_obs_epid(self):
        """Gets the x_obs_epid of this CreateBucketRequest.

        企业项目id，开通企业项目的用户可以从企业项目服务获取，格式为uuid，默认项目传“0”或者不带该头域，未开通企业项目的用户可以不带该头域。 

        :return: The x_obs_epid of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_epid

    @x_obs_epid.setter
    def x_obs_epid(self, x_obs_epid):
        """Sets the x_obs_epid of this CreateBucketRequest.

        企业项目id，开通企业项目的用户可以从企业项目服务获取，格式为uuid，默认项目传“0”或者不带该头域，未开通企业项目的用户可以不带该头域。 

        :param x_obs_epid: The x_obs_epid of this CreateBucketRequest.
        :type x_obs_epid: str
        """
        self._x_obs_epid = x_obs_epid

    @property
    def x_obs_cluster_type(self):
        """Gets the x_obs_cluster_type of this CreateBucketRequest.

        指定桶是创建在公共集群还是专属集群。 

        :return: The x_obs_cluster_type of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_cluster_type

    @x_obs_cluster_type.setter
    def x_obs_cluster_type(self, x_obs_cluster_type):
        """Sets the x_obs_cluster_type of this CreateBucketRequest.

        指定桶是创建在公共集群还是专属集群。 

        :param x_obs_cluster_type: The x_obs_cluster_type of this CreateBucketRequest.
        :type x_obs_cluster_type: str
        """
        self._x_obs_cluster_type = x_obs_cluster_type

    @property
    def x_obs_location_clustergroup_id(self):
        """Gets the x_obs_location_clustergroup_id of this CreateBucketRequest.

        集群显性化创桶时，指定的集群组ID 

        :return: The x_obs_location_clustergroup_id of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_location_clustergroup_id

    @x_obs_location_clustergroup_id.setter
    def x_obs_location_clustergroup_id(self, x_obs_location_clustergroup_id):
        """Sets the x_obs_location_clustergroup_id of this CreateBucketRequest.

        集群显性化创桶时，指定的集群组ID 

        :param x_obs_location_clustergroup_id: The x_obs_location_clustergroup_id of this CreateBucketRequest.
        :type x_obs_location_clustergroup_id: str
        """
        self._x_obs_location_clustergroup_id = x_obs_location_clustergroup_id

    @property
    def x_obs_ies_location(self):
        """Gets the x_obs_ies_location of this CreateBucketRequest.

        如果是要创建在IES站点上，则指定IES站点的AZ ID。此参数和x-obs-cluster-type不可共存。 

        :return: The x_obs_ies_location of this CreateBucketRequest.
        :rtype: str
        """
        return self._x_obs_ies_location

    @x_obs_ies_location.setter
    def x_obs_ies_location(self, x_obs_ies_location):
        """Sets the x_obs_ies_location of this CreateBucketRequest.

        如果是要创建在IES站点上，则指定IES站点的AZ ID。此参数和x-obs-cluster-type不可共存。 

        :param x_obs_ies_location: The x_obs_ies_location of this CreateBucketRequest.
        :type x_obs_ies_location: str
        """
        self._x_obs_ies_location = x_obs_ies_location

    @property
    def body(self):
        """Gets the body of this CreateBucketRequest.

        :return: The body of this CreateBucketRequest.
        :rtype: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateBucketRequest.

        :param body: The body of this CreateBucketRequest.
        :type body: :class:`huaweicloudsdkobs.v1.CreateBucketRequestBody`
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateBucketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
