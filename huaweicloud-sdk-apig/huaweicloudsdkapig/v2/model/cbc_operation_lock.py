# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbcOperationLock:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lock_scene': 'str',
        'lock_source_id': 'str'
    }

    attribute_map = {
        'lock_scene': 'lock_scene',
        'lock_source_id': 'lock_source_id'
    }

    def __init__(self, lock_scene=None, lock_source_id=None):
        r"""CbcOperationLock

        The model defined in huaweicloud sdk

        :param lock_scene: 限制操作场景： - TO_PERIOD_LOCK：按需转包周期场景锁，不允许进行删除、规格变更、按需转包周期等 - SPEC_CHG_LOCK：包周期规格变更场景锁，不允许进行删除、规格变更等
        :type lock_scene: str
        :param lock_source_id: 发起限制操作对象的标志
        :type lock_source_id: str
        """
        
        

        self._lock_scene = None
        self._lock_source_id = None
        self.discriminator = None

        if lock_scene is not None:
            self.lock_scene = lock_scene
        if lock_source_id is not None:
            self.lock_source_id = lock_source_id

    @property
    def lock_scene(self):
        r"""Gets the lock_scene of this CbcOperationLock.

        限制操作场景： - TO_PERIOD_LOCK：按需转包周期场景锁，不允许进行删除、规格变更、按需转包周期等 - SPEC_CHG_LOCK：包周期规格变更场景锁，不允许进行删除、规格变更等

        :return: The lock_scene of this CbcOperationLock.
        :rtype: str
        """
        return self._lock_scene

    @lock_scene.setter
    def lock_scene(self, lock_scene):
        r"""Sets the lock_scene of this CbcOperationLock.

        限制操作场景： - TO_PERIOD_LOCK：按需转包周期场景锁，不允许进行删除、规格变更、按需转包周期等 - SPEC_CHG_LOCK：包周期规格变更场景锁，不允许进行删除、规格变更等

        :param lock_scene: The lock_scene of this CbcOperationLock.
        :type lock_scene: str
        """
        self._lock_scene = lock_scene

    @property
    def lock_source_id(self):
        r"""Gets the lock_source_id of this CbcOperationLock.

        发起限制操作对象的标志

        :return: The lock_source_id of this CbcOperationLock.
        :rtype: str
        """
        return self._lock_source_id

    @lock_source_id.setter
    def lock_source_id(self, lock_source_id):
        r"""Sets the lock_source_id of this CbcOperationLock.

        发起限制操作对象的标志

        :param lock_source_id: The lock_source_id of this CbcOperationLock.
        :type lock_source_id: str
        """
        self._lock_source_id = lock_source_id

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
        if not isinstance(other, CbcOperationLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
