# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFields:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'upsert': 'dict',
        'set': 'dict',
        'add': 'dict',
        'rmv': 'list[str]',
        'insert': 'dict',
        'delete': 'dict',
        'update_blob': 'UpdateBlob'
    }

    attribute_map = {
        'upsert': 'upsert',
        'set': 'set',
        'add': 'add',
        'rmv': 'rmv',
        'insert': 'insert',
        'delete': 'delete',
        'update_blob': 'update_blob'
    }

    def __init__(self, upsert=None, set=None, add=None, rmv=None, insert=None, delete=None, update_blob=None):
        r"""UpdateFields

        The model defined in huaweicloud sdk

        :param upsert: 文档不存在时，插入该完整文档。
        :type upsert: dict
        :param set: 新增或覆盖更新1个或多个字段的值。 &gt; 禁止修改sortkey的字段。
        :type set: dict
        :param add: 对1个或多个字段做加法运算，并更新为运算后的值。
        :type add: dict
        :param rmv: 删除1个或多个字段。 - 数组元素为待删除字段名。
        :type rmv: list[str]
        :param insert: 插入元素到数组中 &gt; 非数组返回失败。
        :type insert: dict
        :param delete: 从数组中删除某个元素 &gt; 非数组返回失败。
        :type delete: dict
        :param update_blob: 
        :type update_blob: :class:`huaweicloudsdkkvs.v1.UpdateBlob`
        """
        
        

        self._upsert = None
        self._set = None
        self._add = None
        self._rmv = None
        self._insert = None
        self._delete = None
        self._update_blob = None
        self.discriminator = None

        if upsert is not None:
            self.upsert = upsert
        if set is not None:
            self.set = set
        if add is not None:
            self.add = add
        if rmv is not None:
            self.rmv = rmv
        if insert is not None:
            self.insert = insert
        if delete is not None:
            self.delete = delete
        if update_blob is not None:
            self.update_blob = update_blob

    @property
    def upsert(self):
        r"""Gets the upsert of this UpdateFields.

        文档不存在时，插入该完整文档。

        :return: The upsert of this UpdateFields.
        :rtype: dict
        """
        return self._upsert

    @upsert.setter
    def upsert(self, upsert):
        r"""Sets the upsert of this UpdateFields.

        文档不存在时，插入该完整文档。

        :param upsert: The upsert of this UpdateFields.
        :type upsert: dict
        """
        self._upsert = upsert

    @property
    def set(self):
        r"""Gets the set of this UpdateFields.

        新增或覆盖更新1个或多个字段的值。 > 禁止修改sortkey的字段。

        :return: The set of this UpdateFields.
        :rtype: dict
        """
        return self._set

    @set.setter
    def set(self, set):
        r"""Sets the set of this UpdateFields.

        新增或覆盖更新1个或多个字段的值。 > 禁止修改sortkey的字段。

        :param set: The set of this UpdateFields.
        :type set: dict
        """
        self._set = set

    @property
    def add(self):
        r"""Gets the add of this UpdateFields.

        对1个或多个字段做加法运算，并更新为运算后的值。

        :return: The add of this UpdateFields.
        :rtype: dict
        """
        return self._add

    @add.setter
    def add(self, add):
        r"""Sets the add of this UpdateFields.

        对1个或多个字段做加法运算，并更新为运算后的值。

        :param add: The add of this UpdateFields.
        :type add: dict
        """
        self._add = add

    @property
    def rmv(self):
        r"""Gets the rmv of this UpdateFields.

        删除1个或多个字段。 - 数组元素为待删除字段名。

        :return: The rmv of this UpdateFields.
        :rtype: list[str]
        """
        return self._rmv

    @rmv.setter
    def rmv(self, rmv):
        r"""Sets the rmv of this UpdateFields.

        删除1个或多个字段。 - 数组元素为待删除字段名。

        :param rmv: The rmv of this UpdateFields.
        :type rmv: list[str]
        """
        self._rmv = rmv

    @property
    def insert(self):
        r"""Gets the insert of this UpdateFields.

        插入元素到数组中 > 非数组返回失败。

        :return: The insert of this UpdateFields.
        :rtype: dict
        """
        return self._insert

    @insert.setter
    def insert(self, insert):
        r"""Sets the insert of this UpdateFields.

        插入元素到数组中 > 非数组返回失败。

        :param insert: The insert of this UpdateFields.
        :type insert: dict
        """
        self._insert = insert

    @property
    def delete(self):
        r"""Gets the delete of this UpdateFields.

        从数组中删除某个元素 > 非数组返回失败。

        :return: The delete of this UpdateFields.
        :rtype: dict
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this UpdateFields.

        从数组中删除某个元素 > 非数组返回失败。

        :param delete: The delete of this UpdateFields.
        :type delete: dict
        """
        self._delete = delete

    @property
    def update_blob(self):
        r"""Gets the update_blob of this UpdateFields.

        :return: The update_blob of this UpdateFields.
        :rtype: :class:`huaweicloudsdkkvs.v1.UpdateBlob`
        """
        return self._update_blob

    @update_blob.setter
    def update_blob(self, update_blob):
        r"""Sets the update_blob of this UpdateFields.

        :param update_blob: The update_blob of this UpdateFields.
        :type update_blob: :class:`huaweicloudsdkkvs.v1.UpdateBlob`
        """
        self._update_blob = update_blob

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
        if not isinstance(other, UpdateFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
