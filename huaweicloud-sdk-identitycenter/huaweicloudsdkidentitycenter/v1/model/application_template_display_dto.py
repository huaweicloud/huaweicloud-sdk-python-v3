# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationTemplateDisplayDto:

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
        'display': 'DisplayDto',
        'application_type': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'display': 'display',
        'application_type': 'application_type'
    }

    def __init__(self, application_id=None, display=None, application_type=None):
        r"""ApplicationTemplateDisplayDto

        The model defined in huaweicloud sdk

        :param application_id: 应用程序Id,以app-为前缀
        :type application_id: str
        :param display: 
        :type display: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        :param application_type: 应用程序类型
        :type application_type: str
        """
        
        

        self._application_id = None
        self._display = None
        self._application_type = None
        self.discriminator = None

        self.application_id = application_id
        self.display = display
        if application_type is not None:
            self.application_type = application_type

    @property
    def application_id(self):
        r"""Gets the application_id of this ApplicationTemplateDisplayDto.

        应用程序Id,以app-为前缀

        :return: The application_id of this ApplicationTemplateDisplayDto.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ApplicationTemplateDisplayDto.

        应用程序Id,以app-为前缀

        :param application_id: The application_id of this ApplicationTemplateDisplayDto.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def display(self):
        r"""Gets the display of this ApplicationTemplateDisplayDto.

        :return: The display of this ApplicationTemplateDisplayDto.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        """
        return self._display

    @display.setter
    def display(self, display):
        r"""Sets the display of this ApplicationTemplateDisplayDto.

        :param display: The display of this ApplicationTemplateDisplayDto.
        :type display: :class:`huaweicloudsdkidentitycenter.v1.DisplayDto`
        """
        self._display = display

    @property
    def application_type(self):
        r"""Gets the application_type of this ApplicationTemplateDisplayDto.

        应用程序类型

        :return: The application_type of this ApplicationTemplateDisplayDto.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        r"""Sets the application_type of this ApplicationTemplateDisplayDto.

        应用程序类型

        :param application_type: The application_type of this ApplicationTemplateDisplayDto.
        :type application_type: str
        """
        self._application_type = application_type

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
        if not isinstance(other, ApplicationTemplateDisplayDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
