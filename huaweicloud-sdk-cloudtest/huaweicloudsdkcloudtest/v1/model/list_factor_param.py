# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactorParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'type': 'str',
        'name': 'str',
        'parent_node_ids': 'list[str]',
        'asset_id': 'str',
        'creator_num': 'str',
        'mindmap_id': 'str',
        'testpoint_id': 'str',
        'mindmap_node_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'name': 'name',
        'parent_node_ids': 'parent_node_ids',
        'asset_id': 'asset_id',
        'creator_num': 'creator_num',
        'mindmap_id': 'mindmap_id',
        'testpoint_id': 'testpoint_id',
        'mindmap_node_id': 'mindmap_node_id'
    }

    def __init__(self, offset=None, limit=None, type=None, name=None, parent_node_ids=None, asset_id=None, creator_num=None, mindmap_id=None, testpoint_id=None, mindmap_node_id=None):
        r"""ListFactorParam

        The model defined in huaweicloud sdk

        :param offset: 
        :type offset: int
        :param limit: 
        :type limit: int
        :param type: 
        :type type: str
        :param name: 
        :type name: str
        :param parent_node_ids: 
        :type parent_node_ids: list[str]
        :param asset_id: 
        :type asset_id: str
        :param creator_num: 
        :type creator_num: str
        :param mindmap_id: 
        :type mindmap_id: str
        :param testpoint_id: 
        :type testpoint_id: str
        :param mindmap_node_id: 
        :type mindmap_node_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._type = None
        self._name = None
        self._parent_node_ids = None
        self._asset_id = None
        self._creator_num = None
        self._mindmap_id = None
        self._testpoint_id = None
        self._mindmap_node_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if parent_node_ids is not None:
            self.parent_node_ids = parent_node_ids
        if asset_id is not None:
            self.asset_id = asset_id
        if creator_num is not None:
            self.creator_num = creator_num
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id
        if testpoint_id is not None:
            self.testpoint_id = testpoint_id
        if mindmap_node_id is not None:
            self.mindmap_node_id = mindmap_node_id

    @property
    def offset(self):
        r"""Gets the offset of this ListFactorParam.

        :return: The offset of this ListFactorParam.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactorParam.

        :param offset: The offset of this ListFactorParam.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFactorParam.

        :return: The limit of this ListFactorParam.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactorParam.

        :param limit: The limit of this ListFactorParam.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        r"""Gets the type of this ListFactorParam.

        :return: The type of this ListFactorParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListFactorParam.

        :param type: The type of this ListFactorParam.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ListFactorParam.

        :return: The name of this ListFactorParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFactorParam.

        :param name: The name of this ListFactorParam.
        :type name: str
        """
        self._name = name

    @property
    def parent_node_ids(self):
        r"""Gets the parent_node_ids of this ListFactorParam.

        :return: The parent_node_ids of this ListFactorParam.
        :rtype: list[str]
        """
        return self._parent_node_ids

    @parent_node_ids.setter
    def parent_node_ids(self, parent_node_ids):
        r"""Sets the parent_node_ids of this ListFactorParam.

        :param parent_node_ids: The parent_node_ids of this ListFactorParam.
        :type parent_node_ids: list[str]
        """
        self._parent_node_ids = parent_node_ids

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListFactorParam.

        :return: The asset_id of this ListFactorParam.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListFactorParam.

        :param asset_id: The asset_id of this ListFactorParam.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def creator_num(self):
        r"""Gets the creator_num of this ListFactorParam.

        :return: The creator_num of this ListFactorParam.
        :rtype: str
        """
        return self._creator_num

    @creator_num.setter
    def creator_num(self, creator_num):
        r"""Sets the creator_num of this ListFactorParam.

        :param creator_num: The creator_num of this ListFactorParam.
        :type creator_num: str
        """
        self._creator_num = creator_num

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this ListFactorParam.

        :return: The mindmap_id of this ListFactorParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this ListFactorParam.

        :param mindmap_id: The mindmap_id of this ListFactorParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

    @property
    def testpoint_id(self):
        r"""Gets the testpoint_id of this ListFactorParam.

        :return: The testpoint_id of this ListFactorParam.
        :rtype: str
        """
        return self._testpoint_id

    @testpoint_id.setter
    def testpoint_id(self, testpoint_id):
        r"""Sets the testpoint_id of this ListFactorParam.

        :param testpoint_id: The testpoint_id of this ListFactorParam.
        :type testpoint_id: str
        """
        self._testpoint_id = testpoint_id

    @property
    def mindmap_node_id(self):
        r"""Gets the mindmap_node_id of this ListFactorParam.

        :return: The mindmap_node_id of this ListFactorParam.
        :rtype: str
        """
        return self._mindmap_node_id

    @mindmap_node_id.setter
    def mindmap_node_id(self, mindmap_node_id):
        r"""Sets the mindmap_node_id of this ListFactorParam.

        :param mindmap_node_id: The mindmap_node_id of this ListFactorParam.
        :type mindmap_node_id: str
        """
        self._mindmap_node_id = mindmap_node_id

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
        if not isinstance(other, ListFactorParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
