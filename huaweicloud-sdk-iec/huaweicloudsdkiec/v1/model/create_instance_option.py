# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'with_prefix': 'bool',
        'image_ref': 'str',
        'flavor_ref': 'str',
        'admin_pass': 'str',
        'key_name': 'str',
        'net_config': 'NetConfigInstance',
        'bandwidth': 'BandwidthConfigInstance',
        'root_volume': 'RootVolume',
        'data_volumes': 'list[DataVolume]',
        'count': 'int',
        'security_groups': 'list[SecurityGroupOption]',
        'coverage': 'CoverageInstance',
        'user_data': 'str'
    }

    attribute_map = {
        'name': 'name',
        'with_prefix': 'with_prefix',
        'image_ref': 'image_ref',
        'flavor_ref': 'flavor_ref',
        'admin_pass': 'admin_pass',
        'key_name': 'key_name',
        'net_config': 'net_config',
        'bandwidth': 'bandwidth',
        'root_volume': 'root_volume',
        'data_volumes': 'data_volumes',
        'count': 'count',
        'security_groups': 'security_groups',
        'coverage': 'coverage',
        'user_data': 'user_data'
    }

    def __init__(self, name=None, with_prefix=None, image_ref=None, flavor_ref=None, admin_pass=None, key_name=None, net_config=None, bandwidth=None, root_volume=None, data_volumes=None, count=None, security_groups=None, coverage=None, user_data=None):
        r"""CreateInstanceOption

        The model defined in huaweicloud sdk

        :param name: 边缘资源名称，与边缘实例一一对应。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-48]个字符。
        :type name: str
        :param with_prefix: 是否自动添加前缀。 - with_prefix为false时不拼接IEC前缀 - with_prefix不传或者传true时拼自动IEC前缀  以name为iec为例： 不添加前缀时实例名称为：iec 自动添加前缀实例名称为：IEC-ZS01-iec
        :type with_prefix: bool
        :param image_ref: 边缘实例的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。 镜像的ID可以从控制台或者参考本文档的“查询边镜像列表”的章节获取。
        :type image_ref: str
        :param flavor_ref: 边缘实例的系统规格的ID。 已上线的规格请使用接口 “查询边缘实例规格列表“ 进行查询。
        :type flavor_ref: str
        :param admin_pass: 如果需要使用密码方式登录边缘实例，可使用adminPass字段指定边缘实例管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。 密码复杂度要求： 1. 长度为8-26位。 2. 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_&#x3D;+[{}]:,./?）中的三种。 3. 密码不能包含用户名或用户名的逆序。 4. Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 说明 目前边缘实例不支持创建后设置密码，不设置此参数会导致实例创建后无法登录。
        :type admin_pass: str
        :param key_name: 密钥对名称。
        :type key_name: str
        :param net_config: 
        :type net_config: :class:`huaweicloudsdkiec.v1.NetConfigInstance`
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkiec.v1.BandwidthConfigInstance`
        :param root_volume: 
        :type root_volume: :class:`huaweicloudsdkiec.v1.RootVolume`
        :param data_volumes: 边缘实例对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。 约束：目前边缘实例最多可挂载2块数据盘
        :type data_volumes: list[:class:`huaweicloudsdkiec.v1.DataVolume`]
        :param count: 边缘实例数量。
        :type count: int
        :param security_groups: 边缘业务对应安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.SecurityGroupOption`]
        :param coverage: 
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageInstance`
        :param user_data: 创建边缘实例过程中注入用户数据。支持注入文本、文本文件或gzip文件。 更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。    
        :type user_data: str
        """
        
        

        self._name = None
        self._with_prefix = None
        self._image_ref = None
        self._flavor_ref = None
        self._admin_pass = None
        self._key_name = None
        self._net_config = None
        self._bandwidth = None
        self._root_volume = None
        self._data_volumes = None
        self._count = None
        self._security_groups = None
        self._coverage = None
        self._user_data = None
        self.discriminator = None

        self.name = name
        if with_prefix is not None:
            self.with_prefix = with_prefix
        self.image_ref = image_ref
        self.flavor_ref = flavor_ref
        if admin_pass is not None:
            self.admin_pass = admin_pass
        if key_name is not None:
            self.key_name = key_name
        self.net_config = net_config
        if bandwidth is not None:
            self.bandwidth = bandwidth
        self.root_volume = root_volume
        if data_volumes is not None:
            self.data_volumes = data_volumes
        self.count = count
        if security_groups is not None:
            self.security_groups = security_groups
        self.coverage = coverage
        if user_data is not None:
            self.user_data = user_data

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceOption.

        边缘资源名称，与边缘实例一一对应。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-48]个字符。

        :return: The name of this CreateInstanceOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceOption.

        边缘资源名称，与边缘实例一一对应。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-48]个字符。

        :param name: The name of this CreateInstanceOption.
        :type name: str
        """
        self._name = name

    @property
    def with_prefix(self):
        r"""Gets the with_prefix of this CreateInstanceOption.

        是否自动添加前缀。 - with_prefix为false时不拼接IEC前缀 - with_prefix不传或者传true时拼自动IEC前缀  以name为iec为例： 不添加前缀时实例名称为：iec 自动添加前缀实例名称为：IEC-ZS01-iec

        :return: The with_prefix of this CreateInstanceOption.
        :rtype: bool
        """
        return self._with_prefix

    @with_prefix.setter
    def with_prefix(self, with_prefix):
        r"""Sets the with_prefix of this CreateInstanceOption.

        是否自动添加前缀。 - with_prefix为false时不拼接IEC前缀 - with_prefix不传或者传true时拼自动IEC前缀  以name为iec为例： 不添加前缀时实例名称为：iec 自动添加前缀实例名称为：IEC-ZS01-iec

        :param with_prefix: The with_prefix of this CreateInstanceOption.
        :type with_prefix: bool
        """
        self._with_prefix = with_prefix

    @property
    def image_ref(self):
        r"""Gets the image_ref of this CreateInstanceOption.

        边缘实例的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。 镜像的ID可以从控制台或者参考本文档的“查询边镜像列表”的章节获取。

        :return: The image_ref of this CreateInstanceOption.
        :rtype: str
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        r"""Sets the image_ref of this CreateInstanceOption.

        边缘实例的系统镜像，需要指定已创建镜像的ID，ID格式为通用唯一识别码（Universally Unique Identifier，简称UUID）。 镜像的ID可以从控制台或者参考本文档的“查询边镜像列表”的章节获取。

        :param image_ref: The image_ref of this CreateInstanceOption.
        :type image_ref: str
        """
        self._image_ref = image_ref

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreateInstanceOption.

        边缘实例的系统规格的ID。 已上线的规格请使用接口 “查询边缘实例规格列表“ 进行查询。

        :return: The flavor_ref of this CreateInstanceOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreateInstanceOption.

        边缘实例的系统规格的ID。 已上线的规格请使用接口 “查询边缘实例规格列表“ 进行查询。

        :param flavor_ref: The flavor_ref of this CreateInstanceOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def admin_pass(self):
        r"""Gets the admin_pass of this CreateInstanceOption.

        如果需要使用密码方式登录边缘实例，可使用adminPass字段指定边缘实例管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。 密码复杂度要求： 1. 长度为8-26位。 2. 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。 3. 密码不能包含用户名或用户名的逆序。 4. Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 说明 目前边缘实例不支持创建后设置密码，不设置此参数会导致实例创建后无法登录。

        :return: The admin_pass of this CreateInstanceOption.
        :rtype: str
        """
        return self._admin_pass

    @admin_pass.setter
    def admin_pass(self, admin_pass):
        r"""Sets the admin_pass of this CreateInstanceOption.

        如果需要使用密码方式登录边缘实例，可使用adminPass字段指定边缘实例管理员帐户初始登录密码。其中，Linux管理员帐户为root，Windows管理员帐户为Administrator。 密码复杂度要求： 1. 长度为8-26位。 2. 密码至少必须包含大写字母、小写字母、数字和特殊字符（!@$%^-_=+[{}]:,./?）中的三种。 3. 密码不能包含用户名或用户名的逆序。 4. Windows系统密码不能包含用户名或用户名的逆序，不能包含用户名中超过两个连续字符的部分。 说明 目前边缘实例不支持创建后设置密码，不设置此参数会导致实例创建后无法登录。

        :param admin_pass: The admin_pass of this CreateInstanceOption.
        :type admin_pass: str
        """
        self._admin_pass = admin_pass

    @property
    def key_name(self):
        r"""Gets the key_name of this CreateInstanceOption.

        密钥对名称。

        :return: The key_name of this CreateInstanceOption.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this CreateInstanceOption.

        密钥对名称。

        :param key_name: The key_name of this CreateInstanceOption.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def net_config(self):
        r"""Gets the net_config of this CreateInstanceOption.

        :return: The net_config of this CreateInstanceOption.
        :rtype: :class:`huaweicloudsdkiec.v1.NetConfigInstance`
        """
        return self._net_config

    @net_config.setter
    def net_config(self, net_config):
        r"""Sets the net_config of this CreateInstanceOption.

        :param net_config: The net_config of this CreateInstanceOption.
        :type net_config: :class:`huaweicloudsdkiec.v1.NetConfigInstance`
        """
        self._net_config = net_config

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this CreateInstanceOption.

        :return: The bandwidth of this CreateInstanceOption.
        :rtype: :class:`huaweicloudsdkiec.v1.BandwidthConfigInstance`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this CreateInstanceOption.

        :param bandwidth: The bandwidth of this CreateInstanceOption.
        :type bandwidth: :class:`huaweicloudsdkiec.v1.BandwidthConfigInstance`
        """
        self._bandwidth = bandwidth

    @property
    def root_volume(self):
        r"""Gets the root_volume of this CreateInstanceOption.

        :return: The root_volume of this CreateInstanceOption.
        :rtype: :class:`huaweicloudsdkiec.v1.RootVolume`
        """
        return self._root_volume

    @root_volume.setter
    def root_volume(self, root_volume):
        r"""Sets the root_volume of this CreateInstanceOption.

        :param root_volume: The root_volume of this CreateInstanceOption.
        :type root_volume: :class:`huaweicloudsdkiec.v1.RootVolume`
        """
        self._root_volume = root_volume

    @property
    def data_volumes(self):
        r"""Gets the data_volumes of this CreateInstanceOption.

        边缘实例对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。 约束：目前边缘实例最多可挂载2块数据盘

        :return: The data_volumes of this CreateInstanceOption.
        :rtype: list[:class:`huaweicloudsdkiec.v1.DataVolume`]
        """
        return self._data_volumes

    @data_volumes.setter
    def data_volumes(self, data_volumes):
        r"""Sets the data_volumes of this CreateInstanceOption.

        边缘实例对应数据盘相关配置。每一个数据结构代表一块待创建的数据盘。 约束：目前边缘实例最多可挂载2块数据盘

        :param data_volumes: The data_volumes of this CreateInstanceOption.
        :type data_volumes: list[:class:`huaweicloudsdkiec.v1.DataVolume`]
        """
        self._data_volumes = data_volumes

    @property
    def count(self):
        r"""Gets the count of this CreateInstanceOption.

        边缘实例数量。

        :return: The count of this CreateInstanceOption.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateInstanceOption.

        边缘实例数量。

        :param count: The count of this CreateInstanceOption.
        :type count: int
        """
        self._count = count

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CreateInstanceOption.

        边缘业务对应安全组信息。

        :return: The security_groups of this CreateInstanceOption.
        :rtype: list[:class:`huaweicloudsdkiec.v1.SecurityGroupOption`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CreateInstanceOption.

        边缘业务对应安全组信息。

        :param security_groups: The security_groups of this CreateInstanceOption.
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.SecurityGroupOption`]
        """
        self._security_groups = security_groups

    @property
    def coverage(self):
        r"""Gets the coverage of this CreateInstanceOption.

        :return: The coverage of this CreateInstanceOption.
        :rtype: :class:`huaweicloudsdkiec.v1.CoverageInstance`
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        r"""Sets the coverage of this CreateInstanceOption.

        :param coverage: The coverage of this CreateInstanceOption.
        :type coverage: :class:`huaweicloudsdkiec.v1.CoverageInstance`
        """
        self._coverage = coverage

    @property
    def user_data(self):
        r"""Gets the user_data of this CreateInstanceOption.

        创建边缘实例过程中注入用户数据。支持注入文本、文本文件或gzip文件。 更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。    

        :return: The user_data of this CreateInstanceOption.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this CreateInstanceOption.

        创建边缘实例过程中注入用户数据。支持注入文本、文本文件或gzip文件。 更多关于待注入用户数据的信息，请参见《弹性云服务器用户指南 》的“[用户数据注入](https://support.huaweicloud.com/usermanual-ecs/zh-cn_topic_0032380449.html)”章节。    

        :param user_data: The user_data of this CreateInstanceOption.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, CreateInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
