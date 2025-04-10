# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserSettingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation': 'Operation',
        'settings': 'UserSettingDto'
    }

    attribute_map = {
        'operation': 'operation',
        'settings': 'settings'
    }

    def __init__(self, operation=None, settings=None):
        r"""ShowUserSettingResponse

        The model defined in huaweicloud sdk

        :param operation: 
        :type operation: :class:`huaweicloudsdkeihealth.v1.Operation`
        :param settings: 
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        
        super(ShowUserSettingResponse, self).__init__()

        self._operation = None
        self._settings = None
        self.discriminator = None

        if operation is not None:
            self.operation = operation
        if settings is not None:
            self.settings = settings

    @property
    def operation(self):
        r"""Gets the operation of this ShowUserSettingResponse.

        :return: The operation of this ShowUserSettingResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.Operation`
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ShowUserSettingResponse.

        :param operation: The operation of this ShowUserSettingResponse.
        :type operation: :class:`huaweicloudsdkeihealth.v1.Operation`
        """
        self._operation = operation

    @property
    def settings(self):
        r"""Gets the settings of this ShowUserSettingResponse.

        :return: The settings of this ShowUserSettingResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        r"""Sets the settings of this ShowUserSettingResponse.

        :param settings: The settings of this ShowUserSettingResponse.
        :type settings: :class:`huaweicloudsdkeihealth.v1.UserSettingDto`
        """
        self._settings = settings

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
        if not isinstance(other, ShowUserSettingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
