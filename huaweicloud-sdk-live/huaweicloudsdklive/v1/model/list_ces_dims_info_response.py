# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCesDimsInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'CesQueryRespQuery'
    }

    attribute_map = {
        'query': 'query'
    }

    def __init__(self, query=None):
        r"""ListCesDimsInfoResponse

        The model defined in huaweicloud sdk

        :param query: 
        :type query: :class:`huaweicloudsdklive.v1.CesQueryRespQuery`
        """
        
        super(ListCesDimsInfoResponse, self).__init__()

        self._query = None
        self.discriminator = None

        if query is not None:
            self.query = query

    @property
    def query(self):
        r"""Gets the query of this ListCesDimsInfoResponse.

        :return: The query of this ListCesDimsInfoResponse.
        :rtype: :class:`huaweicloudsdklive.v1.CesQueryRespQuery`
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListCesDimsInfoResponse.

        :param query: The query of this ListCesDimsInfoResponse.
        :type query: :class:`huaweicloudsdklive.v1.CesQueryRespQuery`
        """
        self._query = query

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
        if not isinstance(other, ListCesDimsInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
