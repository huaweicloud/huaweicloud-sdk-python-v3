# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFeatureRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature_key': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'feature_key': 'feature_key',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, feature_key=None, limit=None, offset=None):
        r"""ShowFeatureRequest

        The model defined in huaweicloud sdk

        :param feature_key: 特性key, 当前支持： - replication.enable - replication.source_region - replication.destination_regions - replication.destination_dgw_regions - features.backup_double_az
        :type feature_key: str
        :param limit: 每页显示条目数，正整数
        :type limit: int
        :param offset: 偏移值,正整数
        :type offset: int
        """
        
        

        self._feature_key = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.feature_key = feature_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def feature_key(self):
        r"""Gets the feature_key of this ShowFeatureRequest.

        特性key, 当前支持： - replication.enable - replication.source_region - replication.destination_regions - replication.destination_dgw_regions - features.backup_double_az

        :return: The feature_key of this ShowFeatureRequest.
        :rtype: str
        """
        return self._feature_key

    @feature_key.setter
    def feature_key(self, feature_key):
        r"""Sets the feature_key of this ShowFeatureRequest.

        特性key, 当前支持： - replication.enable - replication.source_region - replication.destination_regions - replication.destination_dgw_regions - features.backup_double_az

        :param feature_key: The feature_key of this ShowFeatureRequest.
        :type feature_key: str
        """
        self._feature_key = feature_key

    @property
    def limit(self):
        r"""Gets the limit of this ShowFeatureRequest.

        每页显示条目数，正整数

        :return: The limit of this ShowFeatureRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowFeatureRequest.

        每页显示条目数，正整数

        :param limit: The limit of this ShowFeatureRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowFeatureRequest.

        偏移值,正整数

        :return: The offset of this ShowFeatureRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowFeatureRequest.

        偏移值,正整数

        :param offset: The offset of this ShowFeatureRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowFeatureRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
