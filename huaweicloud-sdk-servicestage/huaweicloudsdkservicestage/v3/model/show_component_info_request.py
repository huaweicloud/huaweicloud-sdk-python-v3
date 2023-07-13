# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'application_id': 'str',
        'expect_fields': 'str'
    }

    attribute_map = {
        'component_id': 'component_id',
        'application_id': 'application_id',
        'expect_fields': 'expect_fields'
    }

    def __init__(self, component_id=None, application_id=None, expect_fields=None):
        """ShowComponentInfoRequest

        The model defined in huaweicloud sdk

        :param component_id: 组件id
        :type component_id: str
        :param application_id: 应用id
        :type application_id: str
        :param expect_fields: 特殊字段
        :type expect_fields: str
        """
        
        

        self._component_id = None
        self._application_id = None
        self._expect_fields = None
        self.discriminator = None

        self.component_id = component_id
        self.application_id = application_id
        if expect_fields is not None:
            self.expect_fields = expect_fields

    @property
    def component_id(self):
        """Gets the component_id of this ShowComponentInfoRequest.

        组件id

        :return: The component_id of this ShowComponentInfoRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ShowComponentInfoRequest.

        组件id

        :param component_id: The component_id of this ShowComponentInfoRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        """Gets the application_id of this ShowComponentInfoRequest.

        应用id

        :return: The application_id of this ShowComponentInfoRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ShowComponentInfoRequest.

        应用id

        :param application_id: The application_id of this ShowComponentInfoRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def expect_fields(self):
        """Gets the expect_fields of this ShowComponentInfoRequest.

        特殊字段

        :return: The expect_fields of this ShowComponentInfoRequest.
        :rtype: str
        """
        return self._expect_fields

    @expect_fields.setter
    def expect_fields(self, expect_fields):
        """Sets the expect_fields of this ShowComponentInfoRequest.

        特殊字段

        :param expect_fields: The expect_fields of this ShowComponentInfoRequest.
        :type expect_fields: str
        """
        self._expect_fields = expect_fields

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
        if not isinstance(other, ShowComponentInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
