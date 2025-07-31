# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePasswordComplexityStatusRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operate_all': 'bool',
        'host_ids': 'list[str]'
    }

    attribute_map = {
        'operate_all': 'operate_all',
        'host_ids': 'host_ids'
    }

    def __init__(self, operate_all=None, host_ids=None):
        r"""ChangePasswordComplexityStatusRequestBody

        The model defined in huaweicloud sdk

        :param operate_all: 是否是全量操作。每次最多处理1000个主机。
        :type operate_all: bool
        :param host_ids: 主机id列表。operate_all&#x3D;ture时不处理host_ids参数。
        :type host_ids: list[str]
        """
        
        

        self._operate_all = None
        self._host_ids = None
        self.discriminator = None

        if operate_all is not None:
            self.operate_all = operate_all
        if host_ids is not None:
            self.host_ids = host_ids

    @property
    def operate_all(self):
        r"""Gets the operate_all of this ChangePasswordComplexityStatusRequestBody.

        是否是全量操作。每次最多处理1000个主机。

        :return: The operate_all of this ChangePasswordComplexityStatusRequestBody.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this ChangePasswordComplexityStatusRequestBody.

        是否是全量操作。每次最多处理1000个主机。

        :param operate_all: The operate_all of this ChangePasswordComplexityStatusRequestBody.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def host_ids(self):
        r"""Gets the host_ids of this ChangePasswordComplexityStatusRequestBody.

        主机id列表。operate_all=ture时不处理host_ids参数。

        :return: The host_ids of this ChangePasswordComplexityStatusRequestBody.
        :rtype: list[str]
        """
        return self._host_ids

    @host_ids.setter
    def host_ids(self, host_ids):
        r"""Sets the host_ids of this ChangePasswordComplexityStatusRequestBody.

        主机id列表。operate_all=ture时不处理host_ids参数。

        :param host_ids: The host_ids of this ChangePasswordComplexityStatusRequestBody.
        :type host_ids: list[str]
        """
        self._host_ids = host_ids

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
        if not isinstance(other, ChangePasswordComplexityStatusRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
