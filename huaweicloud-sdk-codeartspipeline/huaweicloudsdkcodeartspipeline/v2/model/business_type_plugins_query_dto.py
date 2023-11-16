# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessTypePluginsQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_condition': 'str',
        'input_repo_type': 'str',
        'input_source_type': 'str',
        'business_type': 'str',
        'regex_name': 'str'
    }

    attribute_map = {
        'use_condition': 'use_condition',
        'input_repo_type': 'input_repo_type',
        'input_source_type': 'input_source_type',
        'business_type': 'business_type',
        'regex_name': 'regex_name'
    }

    def __init__(self, use_condition=None, input_repo_type=None, input_source_type=None, business_type=None, regex_name=None):
        """BusinessTypePluginsQueryDTO

        The model defined in huaweicloud sdk

        :param use_condition: 用于区分插件为流水线可使用/模板可使用
        :type use_condition: str
        :param input_repo_type: 用于区分源的代码仓类型codehub/gitlab/github等
        :type input_repo_type: str
        :param input_source_type: 用于区分单源/多源的情况
        :type input_source_type: str
        :param business_type: 业务类型
        :type business_type: str
        :param regex_name: 名称
        :type regex_name: str
        """
        
        

        self._use_condition = None
        self._input_repo_type = None
        self._input_source_type = None
        self._business_type = None
        self._regex_name = None
        self.discriminator = None

        if use_condition is not None:
            self.use_condition = use_condition
        if input_repo_type is not None:
            self.input_repo_type = input_repo_type
        if input_source_type is not None:
            self.input_source_type = input_source_type
        if business_type is not None:
            self.business_type = business_type
        if regex_name is not None:
            self.regex_name = regex_name

    @property
    def use_condition(self):
        """Gets the use_condition of this BusinessTypePluginsQueryDTO.

        用于区分插件为流水线可使用/模板可使用

        :return: The use_condition of this BusinessTypePluginsQueryDTO.
        :rtype: str
        """
        return self._use_condition

    @use_condition.setter
    def use_condition(self, use_condition):
        """Sets the use_condition of this BusinessTypePluginsQueryDTO.

        用于区分插件为流水线可使用/模板可使用

        :param use_condition: The use_condition of this BusinessTypePluginsQueryDTO.
        :type use_condition: str
        """
        self._use_condition = use_condition

    @property
    def input_repo_type(self):
        """Gets the input_repo_type of this BusinessTypePluginsQueryDTO.

        用于区分源的代码仓类型codehub/gitlab/github等

        :return: The input_repo_type of this BusinessTypePluginsQueryDTO.
        :rtype: str
        """
        return self._input_repo_type

    @input_repo_type.setter
    def input_repo_type(self, input_repo_type):
        """Sets the input_repo_type of this BusinessTypePluginsQueryDTO.

        用于区分源的代码仓类型codehub/gitlab/github等

        :param input_repo_type: The input_repo_type of this BusinessTypePluginsQueryDTO.
        :type input_repo_type: str
        """
        self._input_repo_type = input_repo_type

    @property
    def input_source_type(self):
        """Gets the input_source_type of this BusinessTypePluginsQueryDTO.

        用于区分单源/多源的情况

        :return: The input_source_type of this BusinessTypePluginsQueryDTO.
        :rtype: str
        """
        return self._input_source_type

    @input_source_type.setter
    def input_source_type(self, input_source_type):
        """Sets the input_source_type of this BusinessTypePluginsQueryDTO.

        用于区分单源/多源的情况

        :param input_source_type: The input_source_type of this BusinessTypePluginsQueryDTO.
        :type input_source_type: str
        """
        self._input_source_type = input_source_type

    @property
    def business_type(self):
        """Gets the business_type of this BusinessTypePluginsQueryDTO.

        业务类型

        :return: The business_type of this BusinessTypePluginsQueryDTO.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this BusinessTypePluginsQueryDTO.

        业务类型

        :param business_type: The business_type of this BusinessTypePluginsQueryDTO.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def regex_name(self):
        """Gets the regex_name of this BusinessTypePluginsQueryDTO.

        名称

        :return: The regex_name of this BusinessTypePluginsQueryDTO.
        :rtype: str
        """
        return self._regex_name

    @regex_name.setter
    def regex_name(self, regex_name):
        """Sets the regex_name of this BusinessTypePluginsQueryDTO.

        名称

        :param regex_name: The regex_name of this BusinessTypePluginsQueryDTO.
        :type regex_name: str
        """
        self._regex_name = regex_name

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
        if not isinstance(other, BusinessTypePluginsQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
