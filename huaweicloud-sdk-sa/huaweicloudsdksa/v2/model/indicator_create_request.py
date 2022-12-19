# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndicatorCreateRequest:

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
        'format_version': 'int',
        'type': 'str',
        'trigger_flag': 'bool',
        'data_object': 'CreateIndicatorDetail'
    }

    attribute_map = {
        'name': 'name',
        'format_version': 'format_version',
        'type': 'type',
        'trigger_flag': 'trigger_flag',
        'data_object': 'data_object'
    }

    def __init__(self, name=None, format_version=None, type=None, trigger_flag=None, data_object=None):
        """IndicatorCreateRequest

        The model defined in huaweicloud sdk

        :param name: 指标名称
        :type name: str
        :param format_version: 版本号
        :type format_version: int
        :param type: 类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）
        :type type: str
        :param trigger_flag: 触发标志
        :type trigger_flag: bool
        :param data_object: 
        :type data_object: :class:`huaweicloudsdksa.v2.CreateIndicatorDetail`
        """
        
        

        self._name = None
        self._format_version = None
        self._type = None
        self._trigger_flag = None
        self._data_object = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if format_version is not None:
            self.format_version = format_version
        if type is not None:
            self.type = type
        if trigger_flag is not None:
            self.trigger_flag = trigger_flag
        if data_object is not None:
            self.data_object = data_object

    @property
    def name(self):
        """Gets the name of this IndicatorCreateRequest.

        指标名称

        :return: The name of this IndicatorCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndicatorCreateRequest.

        指标名称

        :param name: The name of this IndicatorCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def format_version(self):
        """Gets the format_version of this IndicatorCreateRequest.

        版本号

        :return: The format_version of this IndicatorCreateRequest.
        :rtype: int
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        """Sets the format_version of this IndicatorCreateRequest.

        版本号

        :param format_version: The format_version of this IndicatorCreateRequest.
        :type format_version: int
        """
        self._format_version = format_version

    @property
    def type(self):
        """Gets the type of this IndicatorCreateRequest.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :return: The type of this IndicatorCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IndicatorCreateRequest.

        类型（SIMULATION,PLAYBOOK,MANUAL,INSTANCE,DATA_SOURCE）

        :param type: The type of this IndicatorCreateRequest.
        :type type: str
        """
        self._type = type

    @property
    def trigger_flag(self):
        """Gets the trigger_flag of this IndicatorCreateRequest.

        触发标志

        :return: The trigger_flag of this IndicatorCreateRequest.
        :rtype: bool
        """
        return self._trigger_flag

    @trigger_flag.setter
    def trigger_flag(self, trigger_flag):
        """Sets the trigger_flag of this IndicatorCreateRequest.

        触发标志

        :param trigger_flag: The trigger_flag of this IndicatorCreateRequest.
        :type trigger_flag: bool
        """
        self._trigger_flag = trigger_flag

    @property
    def data_object(self):
        """Gets the data_object of this IndicatorCreateRequest.

        :return: The data_object of this IndicatorCreateRequest.
        :rtype: :class:`huaweicloudsdksa.v2.CreateIndicatorDetail`
        """
        return self._data_object

    @data_object.setter
    def data_object(self, data_object):
        """Sets the data_object of this IndicatorCreateRequest.

        :param data_object: The data_object of this IndicatorCreateRequest.
        :type data_object: :class:`huaweicloudsdksa.v2.CreateIndicatorDetail`
        """
        self._data_object = data_object

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
        if not isinstance(other, IndicatorCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
