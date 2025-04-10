# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemandInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'pool_ids': 'list[str]'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'pool_ids': 'pool_ids'
    }

    def __init__(self, pool_id=None, pool_ids=None):
        r"""DemandInstance

        The model defined in huaweicloud sdk

        :param pool_id: 弹性公网IP池。 多线路场景下，将在该弹性公网IP池下创建弹性公网IP。 &gt; 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。
        :type pool_id: str
        :param pool_ids: 线路ID集合。多线路场景下，将在各线路下创建弹性公网IP。
        :type pool_ids: list[str]
        """
        
        

        self._pool_id = None
        self._pool_ids = None
        self.discriminator = None

        if pool_id is not None:
            self.pool_id = pool_id
        if pool_ids is not None:
            self.pool_ids = pool_ids

    @property
    def pool_id(self):
        r"""Gets the pool_id of this DemandInstance.

        弹性公网IP池。 多线路场景下，将在该弹性公网IP池下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :return: The pool_id of this DemandInstance.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this DemandInstance.

        弹性公网IP池。 多线路场景下，将在该弹性公网IP池下创建弹性公网IP。 > 覆盖规则为省级/大区时不支持指定线路ID创建边缘业务。

        :param pool_id: The pool_id of this DemandInstance.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def pool_ids(self):
        r"""Gets the pool_ids of this DemandInstance.

        线路ID集合。多线路场景下，将在各线路下创建弹性公网IP。

        :return: The pool_ids of this DemandInstance.
        :rtype: list[str]
        """
        return self._pool_ids

    @pool_ids.setter
    def pool_ids(self, pool_ids):
        r"""Sets the pool_ids of this DemandInstance.

        线路ID集合。多线路场景下，将在各线路下创建弹性公网IP。

        :param pool_ids: The pool_ids of this DemandInstance.
        :type pool_ids: list[str]
        """
        self._pool_ids = pool_ids

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
        if not isinstance(other, DemandInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
