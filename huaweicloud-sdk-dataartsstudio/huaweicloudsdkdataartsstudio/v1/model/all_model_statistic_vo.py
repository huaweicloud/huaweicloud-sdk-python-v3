# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AllModelStatisticVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'frequent': 'list[ModelStatisticVO]',
        'top': 'list[ModelStatisticVO]',
        'logic': 'list[ModelStatisticVO]',
        'physical': 'list[ModelStatisticVO]',
        'dwr': 'ModelStatisticVO',
        'dm': 'ModelStatisticVO'
    }

    attribute_map = {
        'frequent': 'frequent',
        'top': 'top',
        'logic': 'logic',
        'physical': 'physical',
        'dwr': 'dwr',
        'dm': 'dm'
    }

    def __init__(self, frequent=None, top=None, logic=None, physical=None, dwr=None, dm=None):
        """AllModelStatisticVO

        The model defined in huaweicloud sdk

        :param frequent: 是否为常用。
        :type frequent: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        :param top: 首层模型。
        :type top: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        :param logic: 逻辑模型。
        :type logic: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        :param physical: 物理模型。
        :type physical: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        :param dwr: 
        :type dwr: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        :param dm: 
        :type dm: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        """
        
        

        self._frequent = None
        self._top = None
        self._logic = None
        self._physical = None
        self._dwr = None
        self._dm = None
        self.discriminator = None

        if frequent is not None:
            self.frequent = frequent
        if top is not None:
            self.top = top
        if logic is not None:
            self.logic = logic
        if physical is not None:
            self.physical = physical
        if dwr is not None:
            self.dwr = dwr
        if dm is not None:
            self.dm = dm

    @property
    def frequent(self):
        """Gets the frequent of this AllModelStatisticVO.

        是否为常用。

        :return: The frequent of this AllModelStatisticVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        return self._frequent

    @frequent.setter
    def frequent(self, frequent):
        """Sets the frequent of this AllModelStatisticVO.

        是否为常用。

        :param frequent: The frequent of this AllModelStatisticVO.
        :type frequent: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        self._frequent = frequent

    @property
    def top(self):
        """Gets the top of this AllModelStatisticVO.

        首层模型。

        :return: The top of this AllModelStatisticVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        return self._top

    @top.setter
    def top(self, top):
        """Sets the top of this AllModelStatisticVO.

        首层模型。

        :param top: The top of this AllModelStatisticVO.
        :type top: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        self._top = top

    @property
    def logic(self):
        """Gets the logic of this AllModelStatisticVO.

        逻辑模型。

        :return: The logic of this AllModelStatisticVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this AllModelStatisticVO.

        逻辑模型。

        :param logic: The logic of this AllModelStatisticVO.
        :type logic: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        self._logic = logic

    @property
    def physical(self):
        """Gets the physical of this AllModelStatisticVO.

        物理模型。

        :return: The physical of this AllModelStatisticVO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        return self._physical

    @physical.setter
    def physical(self, physical):
        """Sets the physical of this AllModelStatisticVO.

        物理模型。

        :param physical: The physical of this AllModelStatisticVO.
        :type physical: list[:class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`]
        """
        self._physical = physical

    @property
    def dwr(self):
        """Gets the dwr of this AllModelStatisticVO.

        :return: The dwr of this AllModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        """
        return self._dwr

    @dwr.setter
    def dwr(self, dwr):
        """Sets the dwr of this AllModelStatisticVO.

        :param dwr: The dwr of this AllModelStatisticVO.
        :type dwr: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        """
        self._dwr = dwr

    @property
    def dm(self):
        """Gets the dm of this AllModelStatisticVO.

        :return: The dm of this AllModelStatisticVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        """
        return self._dm

    @dm.setter
    def dm(self, dm):
        """Sets the dm of this AllModelStatisticVO.

        :param dm: The dm of this AllModelStatisticVO.
        :type dm: :class:`huaweicloudsdkdataartsstudio.v1.ModelStatisticVO`
        """
        self._dm = dm

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
        if not isinstance(other, AllModelStatisticVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
