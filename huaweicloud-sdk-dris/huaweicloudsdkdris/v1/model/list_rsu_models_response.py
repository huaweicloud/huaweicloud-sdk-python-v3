# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRsuModelsResponse(SdkResponse):

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
        'rsu_models': 'list[RsuModelSummary]'
    }

    attribute_map = {
        'count': 'count',
        'rsu_models': 'rsu_models'
    }

    def __init__(self, count=None, rsu_models=None):
        r"""ListRsuModelsResponse

        The model defined in huaweicloud sdk

        :param count: **参数说明**：满足查询条件的记录总数。
        :type count: int
        :param rsu_models: **参数说明**：RSU型号信息列表。
        :type rsu_models: list[:class:`huaweicloudsdkdris.v1.RsuModelSummary`]
        """
        
        super(ListRsuModelsResponse, self).__init__()

        self._count = None
        self._rsu_models = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if rsu_models is not None:
            self.rsu_models = rsu_models

    @property
    def count(self):
        r"""Gets the count of this ListRsuModelsResponse.

        **参数说明**：满足查询条件的记录总数。

        :return: The count of this ListRsuModelsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListRsuModelsResponse.

        **参数说明**：满足查询条件的记录总数。

        :param count: The count of this ListRsuModelsResponse.
        :type count: int
        """
        self._count = count

    @property
    def rsu_models(self):
        r"""Gets the rsu_models of this ListRsuModelsResponse.

        **参数说明**：RSU型号信息列表。

        :return: The rsu_models of this ListRsuModelsResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.RsuModelSummary`]
        """
        return self._rsu_models

    @rsu_models.setter
    def rsu_models(self, rsu_models):
        r"""Sets the rsu_models of this ListRsuModelsResponse.

        **参数说明**：RSU型号信息列表。

        :param rsu_models: The rsu_models of this ListRsuModelsResponse.
        :type rsu_models: list[:class:`huaweicloudsdkdris.v1.RsuModelSummary`]
        """
        self._rsu_models = rsu_models

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
        if not isinstance(other, ListRsuModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
