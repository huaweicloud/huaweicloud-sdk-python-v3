# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'version_num': 'str',
        'version_desc': 'str',
        'status': 'str',
        'package_name': 'str',
        'component_attachment_id': 'str',
        'sub_version_id': 'str',
        'connection_config': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version_num': 'version_num',
        'version_desc': 'version_desc',
        'status': 'status',
        'package_name': 'package_name',
        'component_attachment_id': 'component_attachment_id',
        'sub_version_id': 'sub_version_id',
        'connection_config': 'connection_config'
    }

    def __init__(self, id=None, version_num=None, version_desc=None, status=None, package_name=None, component_attachment_id=None, sub_version_id=None, connection_config=None):
        r"""ComponentVersionInfo

        The model defined in huaweicloud sdk

        :param id: 版本ID
        :type id: str
        :param version_num: 版本号
        :type version_num: str
        :param version_desc: 版本描述
        :type version_desc: str
        :param status: 状态
        :type status: str
        :param package_name: 插件所属包
        :type package_name: str
        :param component_attachment_id: 插件的附件id
        :type component_attachment_id: str
        :param sub_version_id: 订阅版本id
        :type sub_version_id: str
        :param connection_config: 操作连接配置List
        :type connection_config: str
        """
        
        

        self._id = None
        self._version_num = None
        self._version_desc = None
        self._status = None
        self._package_name = None
        self._component_attachment_id = None
        self._sub_version_id = None
        self._connection_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version_num is not None:
            self.version_num = version_num
        if version_desc is not None:
            self.version_desc = version_desc
        if status is not None:
            self.status = status
        if package_name is not None:
            self.package_name = package_name
        if component_attachment_id is not None:
            self.component_attachment_id = component_attachment_id
        if sub_version_id is not None:
            self.sub_version_id = sub_version_id
        if connection_config is not None:
            self.connection_config = connection_config

    @property
    def id(self):
        r"""Gets the id of this ComponentVersionInfo.

        版本ID

        :return: The id of this ComponentVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentVersionInfo.

        版本ID

        :param id: The id of this ComponentVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def version_num(self):
        r"""Gets the version_num of this ComponentVersionInfo.

        版本号

        :return: The version_num of this ComponentVersionInfo.
        :rtype: str
        """
        return self._version_num

    @version_num.setter
    def version_num(self, version_num):
        r"""Sets the version_num of this ComponentVersionInfo.

        版本号

        :param version_num: The version_num of this ComponentVersionInfo.
        :type version_num: str
        """
        self._version_num = version_num

    @property
    def version_desc(self):
        r"""Gets the version_desc of this ComponentVersionInfo.

        版本描述

        :return: The version_desc of this ComponentVersionInfo.
        :rtype: str
        """
        return self._version_desc

    @version_desc.setter
    def version_desc(self, version_desc):
        r"""Sets the version_desc of this ComponentVersionInfo.

        版本描述

        :param version_desc: The version_desc of this ComponentVersionInfo.
        :type version_desc: str
        """
        self._version_desc = version_desc

    @property
    def status(self):
        r"""Gets the status of this ComponentVersionInfo.

        状态

        :return: The status of this ComponentVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ComponentVersionInfo.

        状态

        :param status: The status of this ComponentVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def package_name(self):
        r"""Gets the package_name of this ComponentVersionInfo.

        插件所属包

        :return: The package_name of this ComponentVersionInfo.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this ComponentVersionInfo.

        插件所属包

        :param package_name: The package_name of this ComponentVersionInfo.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def component_attachment_id(self):
        r"""Gets the component_attachment_id of this ComponentVersionInfo.

        插件的附件id

        :return: The component_attachment_id of this ComponentVersionInfo.
        :rtype: str
        """
        return self._component_attachment_id

    @component_attachment_id.setter
    def component_attachment_id(self, component_attachment_id):
        r"""Sets the component_attachment_id of this ComponentVersionInfo.

        插件的附件id

        :param component_attachment_id: The component_attachment_id of this ComponentVersionInfo.
        :type component_attachment_id: str
        """
        self._component_attachment_id = component_attachment_id

    @property
    def sub_version_id(self):
        r"""Gets the sub_version_id of this ComponentVersionInfo.

        订阅版本id

        :return: The sub_version_id of this ComponentVersionInfo.
        :rtype: str
        """
        return self._sub_version_id

    @sub_version_id.setter
    def sub_version_id(self, sub_version_id):
        r"""Sets the sub_version_id of this ComponentVersionInfo.

        订阅版本id

        :param sub_version_id: The sub_version_id of this ComponentVersionInfo.
        :type sub_version_id: str
        """
        self._sub_version_id = sub_version_id

    @property
    def connection_config(self):
        r"""Gets the connection_config of this ComponentVersionInfo.

        操作连接配置List

        :return: The connection_config of this ComponentVersionInfo.
        :rtype: str
        """
        return self._connection_config

    @connection_config.setter
    def connection_config(self, connection_config):
        r"""Sets the connection_config of this ComponentVersionInfo.

        操作连接配置List

        :param connection_config: The connection_config of this ComponentVersionInfo.
        :type connection_config: str
        """
        self._connection_config = connection_config

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ComponentVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
