# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFacesBatchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'str'
    }

    attribute_map = {
        'filter': 'filter'
    }

    def __init__(self, filter=None):
        r"""DeleteFacesBatchReq

        The model defined in huaweicloud sdk

        :param filter: [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)
        :type filter: str
        """
        
        

        self._filter = None
        self.discriminator = None

        self.filter = filter

    @property
    def filter(self):
        r"""Gets the filter of this DeleteFacesBatchReq.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :return: The filter of this DeleteFacesBatchReq.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this DeleteFacesBatchReq.

        [过滤条件，参考[filter语法](https://support.huaweicloud.com/api-face/face_02_0014.html)。](tag:hc) [过滤条件，参考[filter语法](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0014.html)。](tag:hk)

        :param filter: The filter of this DeleteFacesBatchReq.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, DeleteFacesBatchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
