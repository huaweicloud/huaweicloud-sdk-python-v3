# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TtscGroupAssetsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'asset_ids': 'list[str]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'asset_ids': 'asset_ids'
    }

    def __init__(self, group_id=None, group_name=None, asset_ids=None):
        r"""TtscGroupAssetsConfig

        The model defined in huaweicloud sdk

        :param group_id: 分组id
        :type group_id: str
        :param group_name: 分组名称
        :type group_name: str
        :param asset_ids: 每个分组的资产id列表
        :type asset_ids: list[str]
        """
        
        

        self._group_id = None
        self._group_name = None
        self._asset_ids = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if asset_ids is not None:
            self.asset_ids = asset_ids

    @property
    def group_id(self):
        r"""Gets the group_id of this TtscGroupAssetsConfig.

        分组id

        :return: The group_id of this TtscGroupAssetsConfig.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this TtscGroupAssetsConfig.

        分组id

        :param group_id: The group_id of this TtscGroupAssetsConfig.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this TtscGroupAssetsConfig.

        分组名称

        :return: The group_name of this TtscGroupAssetsConfig.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this TtscGroupAssetsConfig.

        分组名称

        :param group_name: The group_name of this TtscGroupAssetsConfig.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def asset_ids(self):
        r"""Gets the asset_ids of this TtscGroupAssetsConfig.

        每个分组的资产id列表

        :return: The asset_ids of this TtscGroupAssetsConfig.
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        r"""Sets the asset_ids of this TtscGroupAssetsConfig.

        每个分组的资产id列表

        :param asset_ids: The asset_ids of this TtscGroupAssetsConfig.
        :type asset_ids: list[str]
        """
        self._asset_ids = asset_ids

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
        if not isinstance(other, TtscGroupAssetsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
