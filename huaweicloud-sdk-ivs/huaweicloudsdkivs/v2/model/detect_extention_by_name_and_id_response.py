# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectExtentionByNameAndIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta': 'Meta',
        'result': 'IvsExtentionByNameAndIdResponseBodyResult'
    }

    attribute_map = {
        'meta': 'meta',
        'result': 'result'
    }

    def __init__(self, meta=None, result=None):
        """DetectExtentionByNameAndIdResponse

        The model defined in huaweicloud sdk

        :param meta: 
        :type meta: :class:`huaweicloudsdkivs.v2.Meta`
        :param result: 
        :type result: :class:`huaweicloudsdkivs.v2.IvsExtentionByNameAndIdResponseBodyResult`
        """
        
        super(DetectExtentionByNameAndIdResponse, self).__init__()

        self._meta = None
        self._result = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if result is not None:
            self.result = result

    @property
    def meta(self):
        """Gets the meta of this DetectExtentionByNameAndIdResponse.

        :return: The meta of this DetectExtentionByNameAndIdResponse.
        :rtype: :class:`huaweicloudsdkivs.v2.Meta`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this DetectExtentionByNameAndIdResponse.

        :param meta: The meta of this DetectExtentionByNameAndIdResponse.
        :type meta: :class:`huaweicloudsdkivs.v2.Meta`
        """
        self._meta = meta

    @property
    def result(self):
        """Gets the result of this DetectExtentionByNameAndIdResponse.

        :return: The result of this DetectExtentionByNameAndIdResponse.
        :rtype: :class:`huaweicloudsdkivs.v2.IvsExtentionByNameAndIdResponseBodyResult`
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DetectExtentionByNameAndIdResponse.

        :param result: The result of this DetectExtentionByNameAndIdResponse.
        :type result: :class:`huaweicloudsdkivs.v2.IvsExtentionByNameAndIdResponseBodyResult`
        """
        self._result = result

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
        if not isinstance(other, DetectExtentionByNameAndIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
