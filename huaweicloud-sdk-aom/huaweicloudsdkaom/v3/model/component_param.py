# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'model_id': 'str',
        'model_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'model_id': 'model_id',
        'model_type': 'model_type',
        'name': 'name'
    }

    def __init__(self, description=None, model_id=None, model_type=None, name=None):
        r"""ComponentParam

        The model defined in huaweicloud sdk

        :param description: 组件描述
        :type description: str
        :param model_id: 应用Id、子应用Id,id长度不能超过36位，由大小写字母、数字组成
        :type model_id: str
        :param model_type: 应用、子应用，取值：APPLICATION、SUB_APPLICATION ，不区分大小写
        :type model_type: str
        :param name: 组件名称
        :type name: str
        """
        
        

        self._description = None
        self._model_id = None
        self._model_type = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.model_id = model_id
        self.model_type = model_type
        self.name = name

    @property
    def description(self):
        r"""Gets the description of this ComponentParam.

        组件描述

        :return: The description of this ComponentParam.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentParam.

        组件描述

        :param description: The description of this ComponentParam.
        :type description: str
        """
        self._description = description

    @property
    def model_id(self):
        r"""Gets the model_id of this ComponentParam.

        应用Id、子应用Id,id长度不能超过36位，由大小写字母、数字组成

        :return: The model_id of this ComponentParam.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ComponentParam.

        应用Id、子应用Id,id长度不能超过36位，由大小写字母、数字组成

        :param model_id: The model_id of this ComponentParam.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def model_type(self):
        r"""Gets the model_type of this ComponentParam.

        应用、子应用，取值：APPLICATION、SUB_APPLICATION ，不区分大小写

        :return: The model_type of this ComponentParam.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        r"""Sets the model_type of this ComponentParam.

        应用、子应用，取值：APPLICATION、SUB_APPLICATION ，不区分大小写

        :param model_type: The model_type of this ComponentParam.
        :type model_type: str
        """
        self._model_type = model_type

    @property
    def name(self):
        r"""Gets the name of this ComponentParam.

        组件名称

        :return: The name of this ComponentParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentParam.

        组件名称

        :param name: The name of this ComponentParam.
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
        if not isinstance(other, ComponentParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
