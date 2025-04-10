# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EgTargetDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_project_id': 'str',
        'target_channel_id': 'str',
        'target_region': 'str',
        'cross_region': 'bool',
        'cross_account': 'bool',
        'agency_name': 'str'
    }

    attribute_map = {
        'target_project_id': 'target_project_id',
        'target_channel_id': 'target_channel_id',
        'target_region': 'target_region',
        'cross_region': 'cross_region',
        'cross_account': 'cross_account',
        'agency_name': 'agency_name'
    }

    def __init__(self, target_project_id=None, target_channel_id=None, target_region=None, cross_region=None, cross_account=None, agency_name=None):
        r"""EgTargetDetail

        The model defined in huaweicloud sdk

        :param target_project_id: 目标项目id
        :type target_project_id: str
        :param target_channel_id: 目标通道id
        :type target_channel_id: str
        :param target_region: 目标region
        :type target_region: str
        :param cross_region: 跨region开关
        :type cross_region: bool
        :param cross_account: 跨账号开关
        :type cross_account: bool
        :param agency_name: 委托名称
        :type agency_name: str
        """
        
        

        self._target_project_id = None
        self._target_channel_id = None
        self._target_region = None
        self._cross_region = None
        self._cross_account = None
        self._agency_name = None
        self.discriminator = None

        self.target_project_id = target_project_id
        self.target_channel_id = target_channel_id
        self.target_region = target_region
        if cross_region is not None:
            self.cross_region = cross_region
        if cross_account is not None:
            self.cross_account = cross_account
        self.agency_name = agency_name

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this EgTargetDetail.

        目标项目id

        :return: The target_project_id of this EgTargetDetail.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this EgTargetDetail.

        目标项目id

        :param target_project_id: The target_project_id of this EgTargetDetail.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def target_channel_id(self):
        r"""Gets the target_channel_id of this EgTargetDetail.

        目标通道id

        :return: The target_channel_id of this EgTargetDetail.
        :rtype: str
        """
        return self._target_channel_id

    @target_channel_id.setter
    def target_channel_id(self, target_channel_id):
        r"""Sets the target_channel_id of this EgTargetDetail.

        目标通道id

        :param target_channel_id: The target_channel_id of this EgTargetDetail.
        :type target_channel_id: str
        """
        self._target_channel_id = target_channel_id

    @property
    def target_region(self):
        r"""Gets the target_region of this EgTargetDetail.

        目标region

        :return: The target_region of this EgTargetDetail.
        :rtype: str
        """
        return self._target_region

    @target_region.setter
    def target_region(self, target_region):
        r"""Sets the target_region of this EgTargetDetail.

        目标region

        :param target_region: The target_region of this EgTargetDetail.
        :type target_region: str
        """
        self._target_region = target_region

    @property
    def cross_region(self):
        r"""Gets the cross_region of this EgTargetDetail.

        跨region开关

        :return: The cross_region of this EgTargetDetail.
        :rtype: bool
        """
        return self._cross_region

    @cross_region.setter
    def cross_region(self, cross_region):
        r"""Sets the cross_region of this EgTargetDetail.

        跨region开关

        :param cross_region: The cross_region of this EgTargetDetail.
        :type cross_region: bool
        """
        self._cross_region = cross_region

    @property
    def cross_account(self):
        r"""Gets the cross_account of this EgTargetDetail.

        跨账号开关

        :return: The cross_account of this EgTargetDetail.
        :rtype: bool
        """
        return self._cross_account

    @cross_account.setter
    def cross_account(self, cross_account):
        r"""Sets the cross_account of this EgTargetDetail.

        跨账号开关

        :param cross_account: The cross_account of this EgTargetDetail.
        :type cross_account: bool
        """
        self._cross_account = cross_account

    @property
    def agency_name(self):
        r"""Gets the agency_name of this EgTargetDetail.

        委托名称

        :return: The agency_name of this EgTargetDetail.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this EgTargetDetail.

        委托名称

        :param agency_name: The agency_name of this EgTargetDetail.
        :type agency_name: str
        """
        self._agency_name = agency_name

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
        if not isinstance(other, EgTargetDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
