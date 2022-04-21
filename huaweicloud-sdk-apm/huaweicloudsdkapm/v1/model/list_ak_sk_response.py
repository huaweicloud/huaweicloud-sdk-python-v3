# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAkSkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_ak_sk_models': 'list[AccessAkskVO]'
    }

    attribute_map = {
        'access_ak_sk_models': 'access_ak_sk_models'
    }

    def __init__(self, access_ak_sk_models=None):
        """ListAkSkResponse

        The model defined in huaweicloud sdk

        :param access_ak_sk_models: 
        :type access_ak_sk_models: list[:class:`huaweicloudsdkapm.v1.AccessAkskVO`]
        """
        
        super(ListAkSkResponse, self).__init__()

        self._access_ak_sk_models = None
        self.discriminator = None

        if access_ak_sk_models is not None:
            self.access_ak_sk_models = access_ak_sk_models

    @property
    def access_ak_sk_models(self):
        """Gets the access_ak_sk_models of this ListAkSkResponse.


        :return: The access_ak_sk_models of this ListAkSkResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.AccessAkskVO`]
        """
        return self._access_ak_sk_models

    @access_ak_sk_models.setter
    def access_ak_sk_models(self, access_ak_sk_models):
        """Sets the access_ak_sk_models of this ListAkSkResponse.


        :param access_ak_sk_models: The access_ak_sk_models of this ListAkSkResponse.
        :type access_ak_sk_models: list[:class:`huaweicloudsdkapm.v1.AccessAkskVO`]
        """
        self._access_ak_sk_models = access_ak_sk_models

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
        if not isinstance(other, ListAkSkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
