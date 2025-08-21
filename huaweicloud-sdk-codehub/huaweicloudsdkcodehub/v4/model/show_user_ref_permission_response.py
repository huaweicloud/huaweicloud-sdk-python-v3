# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUserRefPermissionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read': 'UserRefPermissionBasicDto',
        'review': 'UserRefPermissionBasicDto',
        'approval': 'UserRefPermissionBasicDto',
        'create_change': 'UserRefPermissionBasicDto',
        'merge': 'UserRefPermissionBasicDto',
        'create_delete': 'UserRefPermissionBasicDto',
        'push': 'UserRefPermissionBasicDto'
    }

    attribute_map = {
        'read': 'read',
        'review': 'review',
        'approval': 'approval',
        'create_change': 'create_change',
        'merge': 'merge',
        'create_delete': 'create_delete',
        'push': 'push'
    }

    def __init__(self, read=None, review=None, approval=None, create_change=None, merge=None, create_delete=None, push=None):
        r"""ShowUserRefPermissionResponse

        The model defined in huaweicloud sdk

        :param read: 
        :type read: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param review: 
        :type review: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param approval: 
        :type approval: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param create_change: 
        :type create_change: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param merge: 
        :type merge: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param create_delete: 
        :type create_delete: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        :param push: 
        :type push: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        
        super(ShowUserRefPermissionResponse, self).__init__()

        self._read = None
        self._review = None
        self._approval = None
        self._create_change = None
        self._merge = None
        self._create_delete = None
        self._push = None
        self.discriminator = None

        if read is not None:
            self.read = read
        if review is not None:
            self.review = review
        if approval is not None:
            self.approval = approval
        if create_change is not None:
            self.create_change = create_change
        if merge is not None:
            self.merge = merge
        if create_delete is not None:
            self.create_delete = create_delete
        if push is not None:
            self.push = push

    @property
    def read(self):
        r"""Gets the read of this ShowUserRefPermissionResponse.

        :return: The read of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._read

    @read.setter
    def read(self, read):
        r"""Sets the read of this ShowUserRefPermissionResponse.

        :param read: The read of this ShowUserRefPermissionResponse.
        :type read: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._read = read

    @property
    def review(self):
        r"""Gets the review of this ShowUserRefPermissionResponse.

        :return: The review of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._review

    @review.setter
    def review(self, review):
        r"""Sets the review of this ShowUserRefPermissionResponse.

        :param review: The review of this ShowUserRefPermissionResponse.
        :type review: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._review = review

    @property
    def approval(self):
        r"""Gets the approval of this ShowUserRefPermissionResponse.

        :return: The approval of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._approval

    @approval.setter
    def approval(self, approval):
        r"""Sets the approval of this ShowUserRefPermissionResponse.

        :param approval: The approval of this ShowUserRefPermissionResponse.
        :type approval: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._approval = approval

    @property
    def create_change(self):
        r"""Gets the create_change of this ShowUserRefPermissionResponse.

        :return: The create_change of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._create_change

    @create_change.setter
    def create_change(self, create_change):
        r"""Sets the create_change of this ShowUserRefPermissionResponse.

        :param create_change: The create_change of this ShowUserRefPermissionResponse.
        :type create_change: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._create_change = create_change

    @property
    def merge(self):
        r"""Gets the merge of this ShowUserRefPermissionResponse.

        :return: The merge of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._merge

    @merge.setter
    def merge(self, merge):
        r"""Sets the merge of this ShowUserRefPermissionResponse.

        :param merge: The merge of this ShowUserRefPermissionResponse.
        :type merge: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._merge = merge

    @property
    def create_delete(self):
        r"""Gets the create_delete of this ShowUserRefPermissionResponse.

        :return: The create_delete of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._create_delete

    @create_delete.setter
    def create_delete(self, create_delete):
        r"""Sets the create_delete of this ShowUserRefPermissionResponse.

        :param create_delete: The create_delete of this ShowUserRefPermissionResponse.
        :type create_delete: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._create_delete = create_delete

    @property
    def push(self):
        r"""Gets the push of this ShowUserRefPermissionResponse.

        :return: The push of this ShowUserRefPermissionResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        return self._push

    @push.setter
    def push(self, push):
        r"""Sets the push of this ShowUserRefPermissionResponse.

        :param push: The push of this ShowUserRefPermissionResponse.
        :type push: :class:`huaweicloudsdkcodehub.v4.UserRefPermissionBasicDto`
        """
        self._push = push

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
        if not isinstance(other, ShowUserRefPermissionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
