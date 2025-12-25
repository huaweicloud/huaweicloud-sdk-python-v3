# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePipeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'shards': 'int',
        'storage_period': 'int'
    }

    attribute_map = {
        'description': 'description',
        'shards': 'shards',
        'storage_period': 'storage_period'
    }

    def __init__(self, description=None, shards=None, storage_period=None):
        r"""UpdatePipeRequestBody

        The model defined in huaweicloud sdk

        :param description: 描述
        :type description: str
        :param shards: 分区个数；默认创建1个，最大支持创建10个分区
        :type shards: int
        :param storage_period: 数据的保存时间，单位为天；默认30天，取值范围为1~3600
        :type storage_period: int
        """
        
        

        self._description = None
        self._shards = None
        self._storage_period = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if shards is not None:
            self.shards = shards
        if storage_period is not None:
            self.storage_period = storage_period

    @property
    def description(self):
        r"""Gets the description of this UpdatePipeRequestBody.

        描述

        :return: The description of this UpdatePipeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePipeRequestBody.

        描述

        :param description: The description of this UpdatePipeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def shards(self):
        r"""Gets the shards of this UpdatePipeRequestBody.

        分区个数；默认创建1个，最大支持创建10个分区

        :return: The shards of this UpdatePipeRequestBody.
        :rtype: int
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this UpdatePipeRequestBody.

        分区个数；默认创建1个，最大支持创建10个分区

        :param shards: The shards of this UpdatePipeRequestBody.
        :type shards: int
        """
        self._shards = shards

    @property
    def storage_period(self):
        r"""Gets the storage_period of this UpdatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :return: The storage_period of this UpdatePipeRequestBody.
        :rtype: int
        """
        return self._storage_period

    @storage_period.setter
    def storage_period(self, storage_period):
        r"""Sets the storage_period of this UpdatePipeRequestBody.

        数据的保存时间，单位为天；默认30天，取值范围为1~3600

        :param storage_period: The storage_period of this UpdatePipeRequestBody.
        :type storage_period: int
        """
        self._storage_period = storage_period

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePipeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
