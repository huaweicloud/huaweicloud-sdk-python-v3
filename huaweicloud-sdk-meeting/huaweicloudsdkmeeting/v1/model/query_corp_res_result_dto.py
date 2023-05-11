# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCorpResResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'corp_vc_res': 'QueryCorpVcResResultDTO'
    }

    attribute_map = {
        'corp_vc_res': 'corpVcRes'
    }

    def __init__(self, corp_vc_res=None):
        """QueryCorpResResultDTO

        The model defined in huaweicloud sdk

        :param corp_vc_res: 
        :type corp_vc_res: :class:`huaweicloudsdkmeeting.v1.QueryCorpVcResResultDTO`
        """
        
        

        self._corp_vc_res = None
        self.discriminator = None

        if corp_vc_res is not None:
            self.corp_vc_res = corp_vc_res

    @property
    def corp_vc_res(self):
        """Gets the corp_vc_res of this QueryCorpResResultDTO.

        :return: The corp_vc_res of this QueryCorpResResultDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.QueryCorpVcResResultDTO`
        """
        return self._corp_vc_res

    @corp_vc_res.setter
    def corp_vc_res(self, corp_vc_res):
        """Sets the corp_vc_res of this QueryCorpResResultDTO.

        :param corp_vc_res: The corp_vc_res of this QueryCorpResResultDTO.
        :type corp_vc_res: :class:`huaweicloudsdkmeeting.v1.QueryCorpVcResResultDTO`
        """
        self._corp_vc_res = corp_vc_res

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
        if not isinstance(other, QueryCorpResResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
