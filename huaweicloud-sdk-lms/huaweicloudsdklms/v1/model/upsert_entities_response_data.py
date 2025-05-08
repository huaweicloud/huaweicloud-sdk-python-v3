# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpsertEntitiesResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upsert_count': 'int',
        'upsert_ids': 'list[object]'
    }

    attribute_map = {
        'upsert_count': 'upsert_count',
        'upsert_ids': 'upsert_ids'
    }

    def __init__(self, upsert_count=None, upsert_ids=None):
        r"""UpsertEntitiesResponseData

        The model defined in huaweicloud sdk

        :param upsert_count: 更新的entity数量。
        :type upsert_count: int
        :param upsert_ids: 更新成功的entity的primary_key
        :type upsert_ids: list[object]
        """
        
        

        self._upsert_count = None
        self._upsert_ids = None
        self.discriminator = None

        self.upsert_count = upsert_count
        if upsert_ids is not None:
            self.upsert_ids = upsert_ids

    @property
    def upsert_count(self):
        r"""Gets the upsert_count of this UpsertEntitiesResponseData.

        更新的entity数量。

        :return: The upsert_count of this UpsertEntitiesResponseData.
        :rtype: int
        """
        return self._upsert_count

    @upsert_count.setter
    def upsert_count(self, upsert_count):
        r"""Sets the upsert_count of this UpsertEntitiesResponseData.

        更新的entity数量。

        :param upsert_count: The upsert_count of this UpsertEntitiesResponseData.
        :type upsert_count: int
        """
        self._upsert_count = upsert_count

    @property
    def upsert_ids(self):
        r"""Gets the upsert_ids of this UpsertEntitiesResponseData.

        更新成功的entity的primary_key

        :return: The upsert_ids of this UpsertEntitiesResponseData.
        :rtype: list[object]
        """
        return self._upsert_ids

    @upsert_ids.setter
    def upsert_ids(self, upsert_ids):
        r"""Sets the upsert_ids of this UpsertEntitiesResponseData.

        更新成功的entity的primary_key

        :param upsert_ids: The upsert_ids of this UpsertEntitiesResponseData.
        :type upsert_ids: list[object]
        """
        self._upsert_ids = upsert_ids

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
        if not isinstance(other, UpsertEntitiesResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
