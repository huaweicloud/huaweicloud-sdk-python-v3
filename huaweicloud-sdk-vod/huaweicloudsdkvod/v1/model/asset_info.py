# coding: utf-8

import pprint
import re

import six





class AssetInfo:


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
        'status': 'Status',
        'description': 'str',
        'base_info': 'BaseInfo',
        'play_info_array': 'list[PlayInfo]'
    }

    attribute_map = {
        'asset_id': 'asset_id',
        'status': 'status',
        'description': 'description',
        'base_info': 'base_info',
        'play_info_array': 'play_info_array'
    }

    def __init__(self, asset_id=None, status=None, description=None, base_info=None, play_info_array=None):
        """AssetInfo - a model defined in huaweicloud sdk"""
        
        

        self._asset_id = None
        self._status = None
        self._description = None
        self._base_info = None
        self._play_info_array = None
        self.discriminator = None

        if asset_id is not None:
            self.asset_id = asset_id
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if base_info is not None:
            self.base_info = base_info
        if play_info_array is not None:
            self.play_info_array = play_info_array

    @property
    def asset_id(self):
        """Gets the asset_id of this AssetInfo.

        媒体ID<br/> 

        :return: The asset_id of this AssetInfo.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this AssetInfo.

        媒体ID<br/> 

        :param asset_id: The asset_id of this AssetInfo.
        :type: str
        """
        self._asset_id = asset_id

    @property
    def status(self):
        """Gets the status of this AssetInfo.


        :return: The status of this AssetInfo.
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AssetInfo.


        :param status: The status of this AssetInfo.
        :type: Status
        """
        self._status = status

    @property
    def description(self):
        """Gets the description of this AssetInfo.

        媒资描述信息<br/> 

        :return: The description of this AssetInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AssetInfo.

        媒资描述信息<br/> 

        :param description: The description of this AssetInfo.
        :type: str
        """
        self._description = description

    @property
    def base_info(self):
        """Gets the base_info of this AssetInfo.


        :return: The base_info of this AssetInfo.
        :rtype: BaseInfo
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        """Sets the base_info of this AssetInfo.


        :param base_info: The base_info of this AssetInfo.
        :type: BaseInfo
        """
        self._base_info = base_info

    @property
    def play_info_array(self):
        """Gets the play_info_array of this AssetInfo.

        播放信息数组<br/> 

        :return: The play_info_array of this AssetInfo.
        :rtype: list[PlayInfo]
        """
        return self._play_info_array

    @play_info_array.setter
    def play_info_array(self, play_info_array):
        """Sets the play_info_array of this AssetInfo.

        播放信息数组<br/> 

        :param play_info_array: The play_info_array of this AssetInfo.
        :type: list[PlayInfo]
        """
        self._play_info_array = play_info_array

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AssetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
