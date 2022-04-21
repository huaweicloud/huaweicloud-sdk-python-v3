# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRuleRequestBody:

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
        'app_id': 'str',
        'description': 'str',
        'status': 'int',
        'data_parsing_status': 'int'
    }

    attribute_map = {
        'name': 'name',
        'app_id': 'app_id',
        'description': 'description',
        'status': 'status',
        'data_parsing_status': 'data_parsing_status'
    }

    def __init__(self, name=None, app_id=None, description=None, status=None, data_parsing_status=None):
        """CreateRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 规则名称，支持英文大小写，数字，下划线和中划线,长度1-64
        :type name: str
        :param app_id: 应用ID
        :type app_id: str
        :param description: 描述，长度0-200
        :type description: str
        :param status: 规则状态 0-启用 1-停用，不填写时默认为0-启用
        :type status: int
        :param data_parsing_status: 数据解析状态，0-启用 1-停用，不填写时默认为1-禁用
        :type data_parsing_status: int
        """
        
        

        self._name = None
        self._app_id = None
        self._description = None
        self._status = None
        self._data_parsing_status = None
        self.discriminator = None

        self.name = name
        self.app_id = app_id
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if data_parsing_status is not None:
            self.data_parsing_status = data_parsing_status

    @property
    def name(self):
        """Gets the name of this CreateRuleRequestBody.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :return: The name of this CreateRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateRuleRequestBody.

        规则名称，支持英文大小写，数字，下划线和中划线,长度1-64

        :param name: The name of this CreateRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this CreateRuleRequestBody.

        应用ID

        :return: The app_id of this CreateRuleRequestBody.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateRuleRequestBody.

        应用ID

        :param app_id: The app_id of this CreateRuleRequestBody.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def description(self):
        """Gets the description of this CreateRuleRequestBody.

        描述，长度0-200

        :return: The description of this CreateRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRuleRequestBody.

        描述，长度0-200

        :param description: The description of this CreateRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this CreateRuleRequestBody.

        规则状态 0-启用 1-停用，不填写时默认为0-启用

        :return: The status of this CreateRuleRequestBody.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateRuleRequestBody.

        规则状态 0-启用 1-停用，不填写时默认为0-启用

        :param status: The status of this CreateRuleRequestBody.
        :type status: int
        """
        self._status = status

    @property
    def data_parsing_status(self):
        """Gets the data_parsing_status of this CreateRuleRequestBody.

        数据解析状态，0-启用 1-停用，不填写时默认为1-禁用

        :return: The data_parsing_status of this CreateRuleRequestBody.
        :rtype: int
        """
        return self._data_parsing_status

    @data_parsing_status.setter
    def data_parsing_status(self, data_parsing_status):
        """Sets the data_parsing_status of this CreateRuleRequestBody.

        数据解析状态，0-启用 1-停用，不填写时默认为1-禁用

        :param data_parsing_status: The data_parsing_status of this CreateRuleRequestBody.
        :type data_parsing_status: int
        """
        self._data_parsing_status = data_parsing_status

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
        if not isinstance(other, CreateRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
