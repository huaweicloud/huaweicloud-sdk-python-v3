# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizInfoVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'biz_id': 'int',
        'biz_type': 'BizTypeEnum'
    }

    attribute_map = {
        'biz_id': 'biz_id',
        'biz_type': 'biz_type'
    }

    def __init__(self, biz_id=None, biz_type=None):
        """BizInfoVO

        The model defined in huaweicloud sdk

        :param biz_id: 业务ID
        :type biz_id: int
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        
        

        self._biz_id = None
        self._biz_type = None
        self.discriminator = None

        self.biz_id = biz_id
        self.biz_type = biz_type

    @property
    def biz_id(self):
        """Gets the biz_id of this BizInfoVO.

        业务ID

        :return: The biz_id of this BizInfoVO.
        :rtype: int
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this BizInfoVO.

        业务ID

        :param biz_id: The biz_id of this BizInfoVO.
        :type biz_id: int
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        """Gets the biz_type of this BizInfoVO.

        :return: The biz_type of this BizInfoVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this BizInfoVO.

        :param biz_type: The biz_type of this BizInfoVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

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
        if not isinstance(other, BizInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
