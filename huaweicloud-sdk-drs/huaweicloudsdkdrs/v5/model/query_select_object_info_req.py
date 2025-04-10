# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuerySelectObjectInfoReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_names': 'list[str]',
        'type': 'str',
        'is_refresh': 'str'
    }

    attribute_map = {
        'db_names': 'db_names',
        'type': 'type',
        'is_refresh': 'is_refresh'
    }

    def __init__(self, db_names=None, type=None, is_refresh=None):
        r"""QuerySelectObjectInfoReq

        The model defined in huaweicloud sdk

        :param db_names: 查询指定库的信息。
        :type db_names: list[str]
        :param type: 查询对象信息类型，取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。
        :type type: str
        :param is_refresh: 是否强制刷新。取值： - true：是，表示从源库重新查询。 - false：否，表示从已缓存中数据查询。
        :type is_refresh: str
        """
        
        

        self._db_names = None
        self._type = None
        self._is_refresh = None
        self.discriminator = None

        if db_names is not None:
            self.db_names = db_names
        self.type = type
        if is_refresh is not None:
            self.is_refresh = is_refresh

    @property
    def db_names(self):
        r"""Gets the db_names of this QuerySelectObjectInfoReq.

        查询指定库的信息。

        :return: The db_names of this QuerySelectObjectInfoReq.
        :rtype: list[str]
        """
        return self._db_names

    @db_names.setter
    def db_names(self, db_names):
        r"""Sets the db_names of this QuerySelectObjectInfoReq.

        查询指定库的信息。

        :param db_names: The db_names of this QuerySelectObjectInfoReq.
        :type db_names: list[str]
        """
        self._db_names = db_names

    @property
    def type(self):
        r"""Gets the type of this QuerySelectObjectInfoReq.

        查询对象信息类型，取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。

        :return: The type of this QuerySelectObjectInfoReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this QuerySelectObjectInfoReq.

        查询对象信息类型，取值： - source：查询源库对象信息。 - modified：查询已选择的（已同步的和未下发的）对象信息。 - synchronized：查询已同步的（已下发的）对象信息 ， 使用场景在任务处于全量中或者增量中。

        :param type: The type of this QuerySelectObjectInfoReq.
        :type type: str
        """
        self._type = type

    @property
    def is_refresh(self):
        r"""Gets the is_refresh of this QuerySelectObjectInfoReq.

        是否强制刷新。取值： - true：是，表示从源库重新查询。 - false：否，表示从已缓存中数据查询。

        :return: The is_refresh of this QuerySelectObjectInfoReq.
        :rtype: str
        """
        return self._is_refresh

    @is_refresh.setter
    def is_refresh(self, is_refresh):
        r"""Sets the is_refresh of this QuerySelectObjectInfoReq.

        是否强制刷新。取值： - true：是，表示从源库重新查询。 - false：否，表示从已缓存中数据查询。

        :param is_refresh: The is_refresh of this QuerySelectObjectInfoReq.
        :type is_refresh: str
        """
        self._is_refresh = is_refresh

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
        if not isinstance(other, QuerySelectObjectInfoReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
