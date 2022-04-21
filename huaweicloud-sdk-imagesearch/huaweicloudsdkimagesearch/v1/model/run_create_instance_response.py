# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunCreateInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'desc': 'str',
        'register_date': 'int',
        'expired_date': 'int',
        'level': 'int',
        'tags': 'list[str]',
        'status': 'str',
        'instance_name': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'desc': 'desc',
        'register_date': 'registerDate',
        'expired_date': 'expiredDate',
        'level': 'level',
        'tags': 'tags',
        'status': 'status',
        'instance_name': 'instanceName'
    }

    def __init__(self, domain=None, desc=None, register_date=None, expired_date=None, level=None, tags=None, status=None, instance_name=None):
        """RunCreateInstanceResponse

        The model defined in huaweicloud sdk

        :param domain: 模型展示名或领域名称。
        :type domain: str
        :param desc: 描述。
        :type desc: str
        :param register_date: 注册时间。
        :type register_date: int
        :param expired_date: 过期时间，-1表示永不过期。
        :type expired_date: int
        :param level: 规格，即实例的图片数量规格，默认为30000000（单位：张）。
        :type level: int
        :param tags: 图片自定义标签。
        :type tags: list[str]
        :param status: 实例的状态，有以下状态信息：   - NORMAL：正常。   - ARREARAGE：欠费。   - CREATION：创建中。   - CREATION_FAILD：创建失败。   - DELETING：删除中。   - DELETING_FAILED：删除失败。   - ABNORMAL：异常。
        :type status: str
        :param instance_name: 实例名称。
        :type instance_name: str
        """
        
        super(RunCreateInstanceResponse, self).__init__()

        self._domain = None
        self._desc = None
        self._register_date = None
        self._expired_date = None
        self._level = None
        self._tags = None
        self._status = None
        self._instance_name = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if desc is not None:
            self.desc = desc
        if register_date is not None:
            self.register_date = register_date
        if expired_date is not None:
            self.expired_date = expired_date
        if level is not None:
            self.level = level
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if instance_name is not None:
            self.instance_name = instance_name

    @property
    def domain(self):
        """Gets the domain of this RunCreateInstanceResponse.

        模型展示名或领域名称。

        :return: The domain of this RunCreateInstanceResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RunCreateInstanceResponse.

        模型展示名或领域名称。

        :param domain: The domain of this RunCreateInstanceResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def desc(self):
        """Gets the desc of this RunCreateInstanceResponse.

        描述。

        :return: The desc of this RunCreateInstanceResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this RunCreateInstanceResponse.

        描述。

        :param desc: The desc of this RunCreateInstanceResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def register_date(self):
        """Gets the register_date of this RunCreateInstanceResponse.

        注册时间。

        :return: The register_date of this RunCreateInstanceResponse.
        :rtype: int
        """
        return self._register_date

    @register_date.setter
    def register_date(self, register_date):
        """Sets the register_date of this RunCreateInstanceResponse.

        注册时间。

        :param register_date: The register_date of this RunCreateInstanceResponse.
        :type register_date: int
        """
        self._register_date = register_date

    @property
    def expired_date(self):
        """Gets the expired_date of this RunCreateInstanceResponse.

        过期时间，-1表示永不过期。

        :return: The expired_date of this RunCreateInstanceResponse.
        :rtype: int
        """
        return self._expired_date

    @expired_date.setter
    def expired_date(self, expired_date):
        """Sets the expired_date of this RunCreateInstanceResponse.

        过期时间，-1表示永不过期。

        :param expired_date: The expired_date of this RunCreateInstanceResponse.
        :type expired_date: int
        """
        self._expired_date = expired_date

    @property
    def level(self):
        """Gets the level of this RunCreateInstanceResponse.

        规格，即实例的图片数量规格，默认为30000000（单位：张）。

        :return: The level of this RunCreateInstanceResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this RunCreateInstanceResponse.

        规格，即实例的图片数量规格，默认为30000000（单位：张）。

        :param level: The level of this RunCreateInstanceResponse.
        :type level: int
        """
        self._level = level

    @property
    def tags(self):
        """Gets the tags of this RunCreateInstanceResponse.

        图片自定义标签。

        :return: The tags of this RunCreateInstanceResponse.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RunCreateInstanceResponse.

        图片自定义标签。

        :param tags: The tags of this RunCreateInstanceResponse.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this RunCreateInstanceResponse.

        实例的状态，有以下状态信息：   - NORMAL：正常。   - ARREARAGE：欠费。   - CREATION：创建中。   - CREATION_FAILD：创建失败。   - DELETING：删除中。   - DELETING_FAILED：删除失败。   - ABNORMAL：异常。

        :return: The status of this RunCreateInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RunCreateInstanceResponse.

        实例的状态，有以下状态信息：   - NORMAL：正常。   - ARREARAGE：欠费。   - CREATION：创建中。   - CREATION_FAILD：创建失败。   - DELETING：删除中。   - DELETING_FAILED：删除失败。   - ABNORMAL：异常。

        :param status: The status of this RunCreateInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def instance_name(self):
        """Gets the instance_name of this RunCreateInstanceResponse.

        实例名称。

        :return: The instance_name of this RunCreateInstanceResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RunCreateInstanceResponse.

        实例名称。

        :param instance_name: The instance_name of this RunCreateInstanceResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

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
        if not isinstance(other, RunCreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
