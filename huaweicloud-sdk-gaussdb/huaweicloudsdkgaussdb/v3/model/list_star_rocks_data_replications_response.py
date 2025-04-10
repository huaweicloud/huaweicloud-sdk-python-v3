# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListStarRocksDataReplicationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'str',
        'replications': 'list[StarRocksReplicationInfo]',
        'ext_text': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'replications': 'replications',
        'ext_text': 'ext_text'
    }

    def __init__(self, total_count=None, replications=None, ext_text=None):
        r"""ListStarRocksDataReplicationsResponse

        The model defined in huaweicloud sdk

        :param total_count: 查询数据同步任务数。
        :type total_count: str
        :param replications: 数据同步任务信息。
        :type replications: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksReplicationInfo`]
        :param ext_text: 扩展字段。
        :type ext_text: str
        """
        
        super(ListStarRocksDataReplicationsResponse, self).__init__()

        self._total_count = None
        self._replications = None
        self._ext_text = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if replications is not None:
            self.replications = replications
        if ext_text is not None:
            self.ext_text = ext_text

    @property
    def total_count(self):
        r"""Gets the total_count of this ListStarRocksDataReplicationsResponse.

        查询数据同步任务数。

        :return: The total_count of this ListStarRocksDataReplicationsResponse.
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListStarRocksDataReplicationsResponse.

        查询数据同步任务数。

        :param total_count: The total_count of this ListStarRocksDataReplicationsResponse.
        :type total_count: str
        """
        self._total_count = total_count

    @property
    def replications(self):
        r"""Gets the replications of this ListStarRocksDataReplicationsResponse.

        数据同步任务信息。

        :return: The replications of this ListStarRocksDataReplicationsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksReplicationInfo`]
        """
        return self._replications

    @replications.setter
    def replications(self, replications):
        r"""Sets the replications of this ListStarRocksDataReplicationsResponse.

        数据同步任务信息。

        :param replications: The replications of this ListStarRocksDataReplicationsResponse.
        :type replications: list[:class:`huaweicloudsdkgaussdb.v3.StarRocksReplicationInfo`]
        """
        self._replications = replications

    @property
    def ext_text(self):
        r"""Gets the ext_text of this ListStarRocksDataReplicationsResponse.

        扩展字段。

        :return: The ext_text of this ListStarRocksDataReplicationsResponse.
        :rtype: str
        """
        return self._ext_text

    @ext_text.setter
    def ext_text(self, ext_text):
        r"""Sets the ext_text of this ListStarRocksDataReplicationsResponse.

        扩展字段。

        :param ext_text: The ext_text of this ListStarRocksDataReplicationsResponse.
        :type ext_text: str
        """
        self._ext_text = ext_text

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
        if not isinstance(other, ListStarRocksDataReplicationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
