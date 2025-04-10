# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_scope': 'str',
        'target_root_db': 'TargetRootDb',
        'object_info': 'dict(str, DatabaseObject)'
    }

    attribute_map = {
        'object_scope': 'object_scope',
        'target_root_db': 'target_root_db',
        'object_info': 'object_info'
    }

    def __init__(self, object_scope=None, target_root_db=None, object_info=None):
        r"""DbObject

        The model defined in huaweicloud sdk

        :param object_scope: 数据库对象迁移或同步范围。取值： - all：全部迁移。 - database：库级迁移或同步。 - table：表级迁移或同步。
        :type object_scope: str
        :param target_root_db: 
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        :param object_info: 数据库对象迁移或同步信息，object_scope为all时不填，为库级或表级时必填。
        :type object_info: dict(str, DatabaseObject)
        """
        
        

        self._object_scope = None
        self._target_root_db = None
        self._object_info = None
        self.discriminator = None

        self.object_scope = object_scope
        if target_root_db is not None:
            self.target_root_db = target_root_db
        if object_info is not None:
            self.object_info = object_info

    @property
    def object_scope(self):
        r"""Gets the object_scope of this DbObject.

        数据库对象迁移或同步范围。取值： - all：全部迁移。 - database：库级迁移或同步。 - table：表级迁移或同步。

        :return: The object_scope of this DbObject.
        :rtype: str
        """
        return self._object_scope

    @object_scope.setter
    def object_scope(self, object_scope):
        r"""Sets the object_scope of this DbObject.

        数据库对象迁移或同步范围。取值： - all：全部迁移。 - database：库级迁移或同步。 - table：表级迁移或同步。

        :param object_scope: The object_scope of this DbObject.
        :type object_scope: str
        """
        self._object_scope = object_scope

    @property
    def target_root_db(self):
        r"""Gets the target_root_db of this DbObject.

        :return: The target_root_db of this DbObject.
        :rtype: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        return self._target_root_db

    @target_root_db.setter
    def target_root_db(self, target_root_db):
        r"""Sets the target_root_db of this DbObject.

        :param target_root_db: The target_root_db of this DbObject.
        :type target_root_db: :class:`huaweicloudsdkdrs.v5.TargetRootDb`
        """
        self._target_root_db = target_root_db

    @property
    def object_info(self):
        r"""Gets the object_info of this DbObject.

        数据库对象迁移或同步信息，object_scope为all时不填，为库级或表级时必填。

        :return: The object_info of this DbObject.
        :rtype: dict(str, DatabaseObject)
        """
        return self._object_info

    @object_info.setter
    def object_info(self, object_info):
        r"""Sets the object_info of this DbObject.

        数据库对象迁移或同步信息，object_scope为all时不填，为库级或表级时必填。

        :param object_info: The object_info of this DbObject.
        :type object_info: dict(str, DatabaseObject)
        """
        self._object_info = object_info

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
        if not isinstance(other, DbObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
