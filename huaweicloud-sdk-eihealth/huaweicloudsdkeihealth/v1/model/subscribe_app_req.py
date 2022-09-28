# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeAppReq:

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
        'asset_version': 'str',
        'destination_app_name': 'str',
        'destination_app_version': 'str'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'asset_version': 'asset_version',
        'destination_app_name': 'destination_app_name',
        'destination_app_version': 'destination_app_version'
    }

    def __init__(self, asset_id=None, asset_version=None, destination_app_name=None, destination_app_version=None):
        """SubscribeAppReq

        The model defined in huaweicloud sdk

        :param asset_id: 资产id。长度1-128，只能包含字母、数字、下划线和中划线
        :type asset_id: str
        :param asset_version: 资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线
        :type asset_version: str
        :param destination_app_name: 目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。
        :type destination_app_name: str
        :param destination_app_version: 目标应用版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。
        :type destination_app_version: str
        """
        
        

        self._asset_id = None
        self._asset_version = None
        self._destination_app_name = None
        self._destination_app_version = None
        self.discriminator = None

        self.asset_id = asset_id
        self.asset_version = asset_version
        self.destination_app_name = destination_app_name
        self.destination_app_version = destination_app_version

    @property
    def asset_id(self):
        """Gets the asset_id of this SubscribeAppReq.

        资产id。长度1-128，只能包含字母、数字、下划线和中划线

        :return: The asset_id of this SubscribeAppReq.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this SubscribeAppReq.

        资产id。长度1-128，只能包含字母、数字、下划线和中划线

        :param asset_id: The asset_id of this SubscribeAppReq.
        :type asset_id: str
        """
        self._asset_id = asset_id

    @property
    def asset_version(self):
        """Gets the asset_version of this SubscribeAppReq.

        资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线

        :return: The asset_version of this SubscribeAppReq.
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this SubscribeAppReq.

        资产版本。长度1-128，字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线

        :param asset_version: The asset_version of this SubscribeAppReq.
        :type asset_version: str
        """
        self._asset_version = asset_version

    @property
    def destination_app_name(self):
        """Gets the destination_app_name of this SubscribeAppReq.

        目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :return: The destination_app_name of this SubscribeAppReq.
        :rtype: str
        """
        return self._destination_app_name

    @destination_app_name.setter
    def destination_app_name(self, destination_app_name):
        """Sets the destination_app_name of this SubscribeAppReq.

        目标应用名称 取值范围：长度为[1,56]，以大小写字母开头，允许出现中划线(-)、下划线(_)、小写字母和数字，且必须以大小写字母或数字结尾。

        :param destination_app_name: The destination_app_name of this SubscribeAppReq.
        :type destination_app_name: str
        """
        self._destination_app_name = destination_app_name

    @property
    def destination_app_version(self):
        """Gets the destination_app_version of this SubscribeAppReq.

        目标应用版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :return: The destination_app_version of this SubscribeAppReq.
        :rtype: str
        """
        return self._destination_app_version

    @destination_app_version.setter
    def destination_app_version(self, destination_app_version):
        """Sets the destination_app_version of this SubscribeAppReq.

        目标应用版本。取值范围：长度[1,24]，以小写字母或数字或大写字母开头，允许出现中划线，必须以小写字母或数字或大写字母结尾。

        :param destination_app_version: The destination_app_version of this SubscribeAppReq.
        :type destination_app_version: str
        """
        self._destination_app_version = destination_app_version

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
        if not isinstance(other, SubscribeAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
