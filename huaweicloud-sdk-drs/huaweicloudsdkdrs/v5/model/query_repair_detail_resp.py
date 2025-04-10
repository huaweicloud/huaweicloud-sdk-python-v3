# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRepairDetailResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'repair_details': 'list[QueryRepairDetailRespRepairDetails]'
    }

    attribute_map = {
        'count': 'count',
        'repair_details': 'repair_details'
    }

    def __init__(self, count=None, repair_details=None):
        r"""QueryRepairDetailResp

        The model defined in huaweicloud sdk

        :param count: 总数。
        :type count: int
        :param repair_details: 修复详情。
        :type repair_details: list[:class:`huaweicloudsdkdrs.v5.QueryRepairDetailRespRepairDetails`]
        """
        
        

        self._count = None
        self._repair_details = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if repair_details is not None:
            self.repair_details = repair_details

    @property
    def count(self):
        r"""Gets the count of this QueryRepairDetailResp.

        总数。

        :return: The count of this QueryRepairDetailResp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this QueryRepairDetailResp.

        总数。

        :param count: The count of this QueryRepairDetailResp.
        :type count: int
        """
        self._count = count

    @property
    def repair_details(self):
        r"""Gets the repair_details of this QueryRepairDetailResp.

        修复详情。

        :return: The repair_details of this QueryRepairDetailResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.QueryRepairDetailRespRepairDetails`]
        """
        return self._repair_details

    @repair_details.setter
    def repair_details(self, repair_details):
        r"""Sets the repair_details of this QueryRepairDetailResp.

        修复详情。

        :param repair_details: The repair_details of this QueryRepairDetailResp.
        :type repair_details: list[:class:`huaweicloudsdkdrs.v5.QueryRepairDetailRespRepairDetails`]
        """
        self._repair_details = repair_details

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
        if not isinstance(other, QueryRepairDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
