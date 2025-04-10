# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticsRVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_count': 'int',
        'delete_count': 'int',
        'logical_delete_count': 'int',
        'update_count': 'int'
    }

    attribute_map = {
        'create_count': 'createCount',
        'delete_count': 'deleteCount',
        'logical_delete_count': 'logicalDeleteCount',
        'update_count': 'updateCount'
    }

    def __init__(self, create_count=None, delete_count=None, logical_delete_count=None, update_count=None):
        r"""StatisticsRVO

        The model defined in huaweicloud sdk

        :param create_count: **参数解释：**  新增统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type create_count: int
        :param delete_count: **参数解释：**  删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type delete_count: int
        :param logical_delete_count: **参数解释：**  软删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type logical_delete_count: int
        :param update_count: **参数解释：**  更新统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type update_count: int
        """
        
        

        self._create_count = None
        self._delete_count = None
        self._logical_delete_count = None
        self._update_count = None
        self.discriminator = None

        if create_count is not None:
            self.create_count = create_count
        if delete_count is not None:
            self.delete_count = delete_count
        if logical_delete_count is not None:
            self.logical_delete_count = logical_delete_count
        if update_count is not None:
            self.update_count = update_count

    @property
    def create_count(self):
        r"""Gets the create_count of this StatisticsRVO.

        **参数解释：**  新增统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The create_count of this StatisticsRVO.
        :rtype: int
        """
        return self._create_count

    @create_count.setter
    def create_count(self, create_count):
        r"""Sets the create_count of this StatisticsRVO.

        **参数解释：**  新增统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param create_count: The create_count of this StatisticsRVO.
        :type create_count: int
        """
        self._create_count = create_count

    @property
    def delete_count(self):
        r"""Gets the delete_count of this StatisticsRVO.

        **参数解释：**  删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The delete_count of this StatisticsRVO.
        :rtype: int
        """
        return self._delete_count

    @delete_count.setter
    def delete_count(self, delete_count):
        r"""Sets the delete_count of this StatisticsRVO.

        **参数解释：**  删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param delete_count: The delete_count of this StatisticsRVO.
        :type delete_count: int
        """
        self._delete_count = delete_count

    @property
    def logical_delete_count(self):
        r"""Gets the logical_delete_count of this StatisticsRVO.

        **参数解释：**  软删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The logical_delete_count of this StatisticsRVO.
        :rtype: int
        """
        return self._logical_delete_count

    @logical_delete_count.setter
    def logical_delete_count(self, logical_delete_count):
        r"""Sets the logical_delete_count of this StatisticsRVO.

        **参数解释：**  软删除统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param logical_delete_count: The logical_delete_count of this StatisticsRVO.
        :type logical_delete_count: int
        """
        self._logical_delete_count = logical_delete_count

    @property
    def update_count(self):
        r"""Gets the update_count of this StatisticsRVO.

        **参数解释：**  更新统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The update_count of this StatisticsRVO.
        :rtype: int
        """
        return self._update_count

    @update_count.setter
    def update_count(self, update_count):
        r"""Sets the update_count of this StatisticsRVO.

        **参数解释：**  更新统计记录数。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param update_count: The update_count of this StatisticsRVO.
        :type update_count: int
        """
        self._update_count = update_count

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
        if not isinstance(other, StatisticsRVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
