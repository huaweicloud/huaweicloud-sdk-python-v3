# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extra_info': 'ResourceExtraInfo',
        'id': 'str',
        'type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'extra_info': 'extra_info',
        'id': 'id',
        'type': 'type',
        'name': 'name'
    }

    def __init__(self, extra_info=None, id=None, type=None, name=None):
        r"""ResourceCreate

        The model defined in huaweicloud sdk

        :param extra_info: 
        :type extra_info: :class:`huaweicloudsdkcbr.v1.ResourceExtraInfo`
        :param id: 待备份资源id
        :type id: str
        :param type: 待备份资源的类型, 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 裸金属服务器: OS::Ironic::BareMetalServer, 线下本地服务器: OS::Native::Server, 弹性文件系统: OS::Sfs::Turbo, 云桌面：OS::Workspace::DesktopV2
        :type type: str
        :param name: 名称
        :type name: str
        """
        
        

        self._extra_info = None
        self._id = None
        self._type = None
        self._name = None
        self.discriminator = None

        if extra_info is not None:
            self.extra_info = extra_info
        self.id = id
        self.type = type
        if name is not None:
            self.name = name

    @property
    def extra_info(self):
        r"""Gets the extra_info of this ResourceCreate.

        :return: The extra_info of this ResourceCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.ResourceExtraInfo`
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info):
        r"""Sets the extra_info of this ResourceCreate.

        :param extra_info: The extra_info of this ResourceCreate.
        :type extra_info: :class:`huaweicloudsdkcbr.v1.ResourceExtraInfo`
        """
        self._extra_info = extra_info

    @property
    def id(self):
        r"""Gets the id of this ResourceCreate.

        待备份资源id

        :return: The id of this ResourceCreate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResourceCreate.

        待备份资源id

        :param id: The id of this ResourceCreate.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ResourceCreate.

        待备份资源的类型, 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 裸金属服务器: OS::Ironic::BareMetalServer, 线下本地服务器: OS::Native::Server, 弹性文件系统: OS::Sfs::Turbo, 云桌面：OS::Workspace::DesktopV2

        :return: The type of this ResourceCreate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceCreate.

        待备份资源的类型, 云服务器: OS::Nova::Server, 云硬盘: OS::Cinder::Volume, 裸金属服务器: OS::Ironic::BareMetalServer, 线下本地服务器: OS::Native::Server, 弹性文件系统: OS::Sfs::Turbo, 云桌面：OS::Workspace::DesktopV2

        :param type: The type of this ResourceCreate.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ResourceCreate.

        名称

        :return: The name of this ResourceCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResourceCreate.

        名称

        :param name: The name of this ResourceCreate.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ResourceCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
