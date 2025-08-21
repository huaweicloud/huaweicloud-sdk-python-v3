# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowReviewSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'with_default_review_categories': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'with_default_review_categories': 'with_default_review_categories'
    }

    def __init__(self, repository_id=None, with_default_review_categories=None):
        r"""ShowReviewSettingRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param with_default_review_categories: **参数解释：** 额外返回可勾选检视意见分类和系统预置检视意见分类。 **取值范围：** - true, 返回可勾选检视意见分类和系统预置检视意见分类。 - false, 不返回可勾选检视意见分类和系统预置检视意见分类。
        :type with_default_review_categories: bool
        """
        
        

        self._repository_id = None
        self._with_default_review_categories = None
        self.discriminator = None

        self.repository_id = repository_id
        if with_default_review_categories is not None:
            self.with_default_review_categories = with_default_review_categories

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowReviewSettingRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowReviewSettingRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowReviewSettingRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowReviewSettingRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def with_default_review_categories(self):
        r"""Gets the with_default_review_categories of this ShowReviewSettingRequest.

        **参数解释：** 额外返回可勾选检视意见分类和系统预置检视意见分类。 **取值范围：** - true, 返回可勾选检视意见分类和系统预置检视意见分类。 - false, 不返回可勾选检视意见分类和系统预置检视意见分类。

        :return: The with_default_review_categories of this ShowReviewSettingRequest.
        :rtype: bool
        """
        return self._with_default_review_categories

    @with_default_review_categories.setter
    def with_default_review_categories(self, with_default_review_categories):
        r"""Sets the with_default_review_categories of this ShowReviewSettingRequest.

        **参数解释：** 额外返回可勾选检视意见分类和系统预置检视意见分类。 **取值范围：** - true, 返回可勾选检视意见分类和系统预置检视意见分类。 - false, 不返回可勾选检视意见分类和系统预置检视意见分类。

        :param with_default_review_categories: The with_default_review_categories of this ShowReviewSettingRequest.
        :type with_default_review_categories: bool
        """
        self._with_default_review_categories = with_default_review_categories

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
        if not isinstance(other, ShowReviewSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
