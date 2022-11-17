# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetTagsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_temp_id': 'int',
        'sim_card_ids': 'list[int]',
        'tag_ids': 'list[int]'
    }

    attribute_map = {
        'file_temp_id': 'file_temp_id',
        'sim_card_ids': 'sim_card_ids',
        'tag_ids': 'tag_ids'
    }

    def __init__(self, file_temp_id=None, sim_card_ids=None, tag_ids=None):
        """BatchSetTagsReq

        The model defined in huaweicloud sdk

        :param file_temp_id: 临时文件ID
        :type file_temp_id: int
        :param sim_card_ids: SIM卡id列表，最多500
        :type sim_card_ids: list[int]
        :param tag_ids: 绑定的标签id列表，最多10
        :type tag_ids: list[int]
        """
        
        

        self._file_temp_id = None
        self._sim_card_ids = None
        self._tag_ids = None
        self.discriminator = None

        if file_temp_id is not None:
            self.file_temp_id = file_temp_id
        if sim_card_ids is not None:
            self.sim_card_ids = sim_card_ids
        if tag_ids is not None:
            self.tag_ids = tag_ids

    @property
    def file_temp_id(self):
        """Gets the file_temp_id of this BatchSetTagsReq.

        临时文件ID

        :return: The file_temp_id of this BatchSetTagsReq.
        :rtype: int
        """
        return self._file_temp_id

    @file_temp_id.setter
    def file_temp_id(self, file_temp_id):
        """Sets the file_temp_id of this BatchSetTagsReq.

        临时文件ID

        :param file_temp_id: The file_temp_id of this BatchSetTagsReq.
        :type file_temp_id: int
        """
        self._file_temp_id = file_temp_id

    @property
    def sim_card_ids(self):
        """Gets the sim_card_ids of this BatchSetTagsReq.

        SIM卡id列表，最多500

        :return: The sim_card_ids of this BatchSetTagsReq.
        :rtype: list[int]
        """
        return self._sim_card_ids

    @sim_card_ids.setter
    def sim_card_ids(self, sim_card_ids):
        """Sets the sim_card_ids of this BatchSetTagsReq.

        SIM卡id列表，最多500

        :param sim_card_ids: The sim_card_ids of this BatchSetTagsReq.
        :type sim_card_ids: list[int]
        """
        self._sim_card_ids = sim_card_ids

    @property
    def tag_ids(self):
        """Gets the tag_ids of this BatchSetTagsReq.

        绑定的标签id列表，最多10

        :return: The tag_ids of this BatchSetTagsReq.
        :rtype: list[int]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this BatchSetTagsReq.

        绑定的标签id列表，最多10

        :param tag_ids: The tag_ids of this BatchSetTagsReq.
        :type tag_ids: list[int]
        """
        self._tag_ids = tag_ids

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
        if not isinstance(other, BatchSetTagsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
