# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCreateAccountStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_account_status': 'CreateAccountStatusDto'
    }

    attribute_map = {
        'create_account_status': 'create_account_status'
    }

    def __init__(self, create_account_status=None):
        r"""ShowCreateAccountStatusResponse

        The model defined in huaweicloud sdk

        :param create_account_status: 
        :type create_account_status: :class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`
        """
        
        super(ShowCreateAccountStatusResponse, self).__init__()

        self._create_account_status = None
        self.discriminator = None

        if create_account_status is not None:
            self.create_account_status = create_account_status

    @property
    def create_account_status(self):
        r"""Gets the create_account_status of this ShowCreateAccountStatusResponse.

        :return: The create_account_status of this ShowCreateAccountStatusResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`
        """
        return self._create_account_status

    @create_account_status.setter
    def create_account_status(self, create_account_status):
        r"""Sets the create_account_status of this ShowCreateAccountStatusResponse.

        :param create_account_status: The create_account_status of this ShowCreateAccountStatusResponse.
        :type create_account_status: :class:`huaweicloudsdkorganizations.v1.CreateAccountStatusDto`
        """
        self._create_account_status = create_account_status

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
        if not isinstance(other, ShowCreateAccountStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
