# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFactoryPendingItemsPackageBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apply_user_id': 'str',
        'package_name': 'str',
        'pending_item_list': 'list[str]',
        'approver_ids': 'list[str]'
    }

    attribute_map = {
        'apply_user_id': 'apply_user_id',
        'package_name': 'package_name',
        'pending_item_list': 'pending_item_list',
        'approver_ids': 'approver_ids'
    }

    def __init__(self, apply_user_id=None, package_name=None, pending_item_list=None, approver_ids=None):
        r"""CreateFactoryPendingItemsPackageBody

        The model defined in huaweicloud sdk

        :param apply_user_id: 发包人id，可从 查询待发布包列表接口 获取。
        :type apply_user_id: str
        :param package_name: 发布包名称
        :type package_name: str
        :param pending_item_list: 待发布包id，可从 查询待发布包列表接口 获取。
        :type pending_item_list: list[str]
        :param approver_ids: 审批人id，可通过管理中心-&gt; 查询空间用户信息 接口 获取，且具有管理员或者部署者权限。
        :type approver_ids: list[str]
        """
        
        

        self._apply_user_id = None
        self._package_name = None
        self._pending_item_list = None
        self._approver_ids = None
        self.discriminator = None

        self.apply_user_id = apply_user_id
        self.package_name = package_name
        self.pending_item_list = pending_item_list
        self.approver_ids = approver_ids

    @property
    def apply_user_id(self):
        r"""Gets the apply_user_id of this CreateFactoryPendingItemsPackageBody.

        发包人id，可从 查询待发布包列表接口 获取。

        :return: The apply_user_id of this CreateFactoryPendingItemsPackageBody.
        :rtype: str
        """
        return self._apply_user_id

    @apply_user_id.setter
    def apply_user_id(self, apply_user_id):
        r"""Sets the apply_user_id of this CreateFactoryPendingItemsPackageBody.

        发包人id，可从 查询待发布包列表接口 获取。

        :param apply_user_id: The apply_user_id of this CreateFactoryPendingItemsPackageBody.
        :type apply_user_id: str
        """
        self._apply_user_id = apply_user_id

    @property
    def package_name(self):
        r"""Gets the package_name of this CreateFactoryPendingItemsPackageBody.

        发布包名称

        :return: The package_name of this CreateFactoryPendingItemsPackageBody.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this CreateFactoryPendingItemsPackageBody.

        发布包名称

        :param package_name: The package_name of this CreateFactoryPendingItemsPackageBody.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def pending_item_list(self):
        r"""Gets the pending_item_list of this CreateFactoryPendingItemsPackageBody.

        待发布包id，可从 查询待发布包列表接口 获取。

        :return: The pending_item_list of this CreateFactoryPendingItemsPackageBody.
        :rtype: list[str]
        """
        return self._pending_item_list

    @pending_item_list.setter
    def pending_item_list(self, pending_item_list):
        r"""Sets the pending_item_list of this CreateFactoryPendingItemsPackageBody.

        待发布包id，可从 查询待发布包列表接口 获取。

        :param pending_item_list: The pending_item_list of this CreateFactoryPendingItemsPackageBody.
        :type pending_item_list: list[str]
        """
        self._pending_item_list = pending_item_list

    @property
    def approver_ids(self):
        r"""Gets the approver_ids of this CreateFactoryPendingItemsPackageBody.

        审批人id，可通过管理中心-> 查询空间用户信息 接口 获取，且具有管理员或者部署者权限。

        :return: The approver_ids of this CreateFactoryPendingItemsPackageBody.
        :rtype: list[str]
        """
        return self._approver_ids

    @approver_ids.setter
    def approver_ids(self, approver_ids):
        r"""Sets the approver_ids of this CreateFactoryPendingItemsPackageBody.

        审批人id，可通过管理中心-> 查询空间用户信息 接口 获取，且具有管理员或者部署者权限。

        :param approver_ids: The approver_ids of this CreateFactoryPendingItemsPackageBody.
        :type approver_ids: list[str]
        """
        self._approver_ids = approver_ids

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
        if not isinstance(other, CreateFactoryPendingItemsPackageBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
