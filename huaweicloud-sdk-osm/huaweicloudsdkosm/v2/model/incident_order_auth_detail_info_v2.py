# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IncidentOrderAuthDetailInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'port': 'int',
        'account': 'str',
        'type': 'int',
        'instance_id': 'str',
        'instance_name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'port': 'port',
        'account': 'account',
        'type': 'type',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'region_id': 'region_id'
    }

    def __init__(self, id=None, port=None, account=None, type=None, instance_id=None, instance_name=None, region_id=None):
        """IncidentOrderAuthDetailInfoV2

        The model defined in huaweicloud sdk

        :param id: 授权详情id
        :type id: int
        :param port: 端口
        :type port: int
        :param account: 账户
        :type account: str
        :param type: 授权详情类型，0控制台 1主机资源
        :type type: int
        :param instance_id: 实例id
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param region_id: 区域id
        :type region_id: str
        """
        
        

        self._id = None
        self._port = None
        self._account = None
        self._type = None
        self._instance_id = None
        self._instance_name = None
        self._region_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if port is not None:
            self.port = port
        if account is not None:
            self.account = account
        if type is not None:
            self.type = type
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if region_id is not None:
            self.region_id = region_id

    @property
    def id(self):
        """Gets the id of this IncidentOrderAuthDetailInfoV2.

        授权详情id

        :return: The id of this IncidentOrderAuthDetailInfoV2.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IncidentOrderAuthDetailInfoV2.

        授权详情id

        :param id: The id of this IncidentOrderAuthDetailInfoV2.
        :type id: int
        """
        self._id = id

    @property
    def port(self):
        """Gets the port of this IncidentOrderAuthDetailInfoV2.

        端口

        :return: The port of this IncidentOrderAuthDetailInfoV2.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this IncidentOrderAuthDetailInfoV2.

        端口

        :param port: The port of this IncidentOrderAuthDetailInfoV2.
        :type port: int
        """
        self._port = port

    @property
    def account(self):
        """Gets the account of this IncidentOrderAuthDetailInfoV2.

        账户

        :return: The account of this IncidentOrderAuthDetailInfoV2.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this IncidentOrderAuthDetailInfoV2.

        账户

        :param account: The account of this IncidentOrderAuthDetailInfoV2.
        :type account: str
        """
        self._account = account

    @property
    def type(self):
        """Gets the type of this IncidentOrderAuthDetailInfoV2.

        授权详情类型，0控制台 1主机资源

        :return: The type of this IncidentOrderAuthDetailInfoV2.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IncidentOrderAuthDetailInfoV2.

        授权详情类型，0控制台 1主机资源

        :param type: The type of this IncidentOrderAuthDetailInfoV2.
        :type type: int
        """
        self._type = type

    @property
    def instance_id(self):
        """Gets the instance_id of this IncidentOrderAuthDetailInfoV2.

        实例id

        :return: The instance_id of this IncidentOrderAuthDetailInfoV2.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this IncidentOrderAuthDetailInfoV2.

        实例id

        :param instance_id: The instance_id of this IncidentOrderAuthDetailInfoV2.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this IncidentOrderAuthDetailInfoV2.

        实例名称

        :return: The instance_name of this IncidentOrderAuthDetailInfoV2.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this IncidentOrderAuthDetailInfoV2.

        实例名称

        :param instance_name: The instance_name of this IncidentOrderAuthDetailInfoV2.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def region_id(self):
        """Gets the region_id of this IncidentOrderAuthDetailInfoV2.

        区域id

        :return: The region_id of this IncidentOrderAuthDetailInfoV2.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this IncidentOrderAuthDetailInfoV2.

        区域id

        :param region_id: The region_id of this IncidentOrderAuthDetailInfoV2.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, IncidentOrderAuthDetailInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
