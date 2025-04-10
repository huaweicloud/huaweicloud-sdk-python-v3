# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackUpMindmapParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bak_name': 'str',
        'memo': 'str',
        'mindmap_id': 'str'
    }

    attribute_map = {
        'bak_name': 'bak_name',
        'memo': 'memo',
        'mindmap_id': 'mindmap_id'
    }

    def __init__(self, bak_name=None, memo=None, mindmap_id=None):
        r"""BackUpMindmapParam

        The model defined in huaweicloud sdk

        :param bak_name: 备份名称
        :type bak_name: str
        :param memo: 备注
        :type memo: str
        :param mindmap_id: 脑图id
        :type mindmap_id: str
        """
        
        

        self._bak_name = None
        self._memo = None
        self._mindmap_id = None
        self.discriminator = None

        if bak_name is not None:
            self.bak_name = bak_name
        if memo is not None:
            self.memo = memo
        if mindmap_id is not None:
            self.mindmap_id = mindmap_id

    @property
    def bak_name(self):
        r"""Gets the bak_name of this BackUpMindmapParam.

        备份名称

        :return: The bak_name of this BackUpMindmapParam.
        :rtype: str
        """
        return self._bak_name

    @bak_name.setter
    def bak_name(self, bak_name):
        r"""Sets the bak_name of this BackUpMindmapParam.

        备份名称

        :param bak_name: The bak_name of this BackUpMindmapParam.
        :type bak_name: str
        """
        self._bak_name = bak_name

    @property
    def memo(self):
        r"""Gets the memo of this BackUpMindmapParam.

        备注

        :return: The memo of this BackUpMindmapParam.
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        r"""Sets the memo of this BackUpMindmapParam.

        备注

        :param memo: The memo of this BackUpMindmapParam.
        :type memo: str
        """
        self._memo = memo

    @property
    def mindmap_id(self):
        r"""Gets the mindmap_id of this BackUpMindmapParam.

        脑图id

        :return: The mindmap_id of this BackUpMindmapParam.
        :rtype: str
        """
        return self._mindmap_id

    @mindmap_id.setter
    def mindmap_id(self, mindmap_id):
        r"""Sets the mindmap_id of this BackUpMindmapParam.

        脑图id

        :param mindmap_id: The mindmap_id of this BackUpMindmapParam.
        :type mindmap_id: str
        """
        self._mindmap_id = mindmap_id

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
        if not isinstance(other, BackUpMindmapParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
