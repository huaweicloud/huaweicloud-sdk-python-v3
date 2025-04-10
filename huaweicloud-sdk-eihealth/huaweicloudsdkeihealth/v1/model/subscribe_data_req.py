# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeDataReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_id': 'str',
        'overwrite': 'bool',
        'target_folder': 'str',
        'version': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'overwrite': 'overwrite',
        'target_folder': 'target_folder',
        'version': 'version'
    }

    def __init__(self, asset_id=None, overwrite=None, target_folder=None, version=None):
        r"""SubscribeDataReq

        The model defined in huaweicloud sdk

        :param asset_id: 资产ID
        :type asset_id: str
        :param overwrite: 执行策略（true：全部覆盖，false：全部跳过，默认为true）
        :type overwrite: bool
        :param target_folder: 目标文件夹
        :type target_folder: str
        :param version: 版本号
        :type version: str
        """
        
        

        self._asset_id = None
        self._overwrite = None
        self._target_folder = None
        self._version = None
        self.discriminator = None

        self.asset_id = asset_id
        if overwrite is not None:
            self.overwrite = overwrite
        if target_folder is not None:
            self.target_folder = target_folder
        self.version = version

    @property
    def asset_id(self):
        r"""Gets the asset_id of this SubscribeDataReq.

        资产ID

        :return: The asset_id of this SubscribeDataReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this SubscribeDataReq.

        资产ID

        :param asset_id: The asset_id of this SubscribeDataReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def overwrite(self):
        r"""Gets the overwrite of this SubscribeDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :return: The overwrite of this SubscribeDataReq.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        r"""Sets the overwrite of this SubscribeDataReq.

        执行策略（true：全部覆盖，false：全部跳过，默认为true）

        :param overwrite: The overwrite of this SubscribeDataReq.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def target_folder(self):
        r"""Gets the target_folder of this SubscribeDataReq.

        目标文件夹

        :return: The target_folder of this SubscribeDataReq.
        :rtype: str
        """
        return self._target_folder

    @target_folder.setter
    def target_folder(self, target_folder):
        r"""Sets the target_folder of this SubscribeDataReq.

        目标文件夹

        :param target_folder: The target_folder of this SubscribeDataReq.
        :type target_folder: str
        """
        self._target_folder = target_folder

    @property
    def version(self):
        r"""Gets the version of this SubscribeDataReq.

        版本号

        :return: The version of this SubscribeDataReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SubscribeDataReq.

        版本号

        :param version: The version of this SubscribeDataReq.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, SubscribeDataReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
