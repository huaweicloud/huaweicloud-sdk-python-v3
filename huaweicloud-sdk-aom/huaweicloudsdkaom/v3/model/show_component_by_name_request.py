# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentByNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_name': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_name': 'component_name'
    }

    def __init__(self, application_id=None, component_name=None):
        r"""ShowComponentByNameRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用id
        :type application_id: str
        :param component_name: 组件名称
        :type component_name: str
        """
        
        

        self._application_id = None
        self._component_name = None
        self.discriminator = None

        self.application_id = application_id
        self.component_name = component_name

    @property
    def application_id(self):
        r"""Gets the application_id of this ShowComponentByNameRequest.

        应用id

        :return: The application_id of this ShowComponentByNameRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ShowComponentByNameRequest.

        应用id

        :param application_id: The application_id of this ShowComponentByNameRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_name(self):
        r"""Gets the component_name of this ShowComponentByNameRequest.

        组件名称

        :return: The component_name of this ShowComponentByNameRequest.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this ShowComponentByNameRequest.

        组件名称

        :param component_name: The component_name of this ShowComponentByNameRequest.
        :type component_name: str
        """
        self._component_name = component_name

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
        if not isinstance(other, ShowComponentByNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
