# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBpaRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "PublicAccessBlockConfiguration"

    sensitive_list = []

    openapi_types = {
        'block_public_acls': 'bool',
        'block_public_policy': 'bool',
        'ignore_public_acls': 'bool',
        'restrict_public_buckets': 'bool'
    }

    attribute_map = {
        'block_public_acls': 'BlockPublicAcls',
        'block_public_policy': 'BlockPublicPolicy',
        'ignore_public_acls': 'IgnorePublicAcls',
        'restrict_public_buckets': 'RestrictPublicBuckets'
    }

    def __init__(self, block_public_acls=None, block_public_policy=None, ignore_public_acls=None, restrict_public_buckets=None):
        r"""SetBpaRequestBody

        The model defined in huaweicloud sdk

        :param block_public_acls: Whether to prohibit specifying the ACL as public access to a bucket or objects in the bucket. If the parameter is set to true, the following applies: If you specify an ACL as public access when uploading an object, the object fails to be uploaded and the error \&quot;403 Access Denied\&quot; is returned. If you specify an ACL as public access when modifying a bucket ACL or an object ACL, the ACL fails to be modified and the error \&quot;403 Access Denied\&quot; is returned.
        :type block_public_acls: bool
        :param block_public_policy: Whether to prohibit the configuration of a bucket policy that allows public access to a bucket. If this parameter is set to true, such a bucket policy will fail to be configured and the error \&quot;403 Access Denied\&quot; will be returned.
        :type block_public_policy: bool
        :param ignore_public_acls: Whether to ignore the existing ACL that allows public access to the bucket or objects in the bucket. If this parameter is set to true, the public access ACL of the bucket or objects in the bucket becomes invalid.
        :type ignore_public_acls: bool
        :param restrict_public_buckets: Whether to restrict the existing public bucket policy. If this parameter is set to true, only the cloud service and bucket owner accounts are allowed to access the bucket.
        :type restrict_public_buckets: bool
        """
        
        

        self._block_public_acls = None
        self._block_public_policy = None
        self._ignore_public_acls = None
        self._restrict_public_buckets = None
        self.discriminator = None

        if block_public_acls is not None:
            self.block_public_acls = block_public_acls
        if block_public_policy is not None:
            self.block_public_policy = block_public_policy
        if ignore_public_acls is not None:
            self.ignore_public_acls = ignore_public_acls
        if restrict_public_buckets is not None:
            self.restrict_public_buckets = restrict_public_buckets

    @property
    def block_public_acls(self):
        r"""Gets the block_public_acls of this SetBpaRequestBody.

        Whether to prohibit specifying the ACL as public access to a bucket or objects in the bucket. If the parameter is set to true, the following applies: If you specify an ACL as public access when uploading an object, the object fails to be uploaded and the error \"403 Access Denied\" is returned. If you specify an ACL as public access when modifying a bucket ACL or an object ACL, the ACL fails to be modified and the error \"403 Access Denied\" is returned.

        :return: The block_public_acls of this SetBpaRequestBody.
        :rtype: bool
        """
        return self._block_public_acls

    @block_public_acls.setter
    def block_public_acls(self, block_public_acls):
        r"""Sets the block_public_acls of this SetBpaRequestBody.

        Whether to prohibit specifying the ACL as public access to a bucket or objects in the bucket. If the parameter is set to true, the following applies: If you specify an ACL as public access when uploading an object, the object fails to be uploaded and the error \"403 Access Denied\" is returned. If you specify an ACL as public access when modifying a bucket ACL or an object ACL, the ACL fails to be modified and the error \"403 Access Denied\" is returned.

        :param block_public_acls: The block_public_acls of this SetBpaRequestBody.
        :type block_public_acls: bool
        """
        self._block_public_acls = block_public_acls

    @property
    def block_public_policy(self):
        r"""Gets the block_public_policy of this SetBpaRequestBody.

        Whether to prohibit the configuration of a bucket policy that allows public access to a bucket. If this parameter is set to true, such a bucket policy will fail to be configured and the error \"403 Access Denied\" will be returned.

        :return: The block_public_policy of this SetBpaRequestBody.
        :rtype: bool
        """
        return self._block_public_policy

    @block_public_policy.setter
    def block_public_policy(self, block_public_policy):
        r"""Sets the block_public_policy of this SetBpaRequestBody.

        Whether to prohibit the configuration of a bucket policy that allows public access to a bucket. If this parameter is set to true, such a bucket policy will fail to be configured and the error \"403 Access Denied\" will be returned.

        :param block_public_policy: The block_public_policy of this SetBpaRequestBody.
        :type block_public_policy: bool
        """
        self._block_public_policy = block_public_policy

    @property
    def ignore_public_acls(self):
        r"""Gets the ignore_public_acls of this SetBpaRequestBody.

        Whether to ignore the existing ACL that allows public access to the bucket or objects in the bucket. If this parameter is set to true, the public access ACL of the bucket or objects in the bucket becomes invalid.

        :return: The ignore_public_acls of this SetBpaRequestBody.
        :rtype: bool
        """
        return self._ignore_public_acls

    @ignore_public_acls.setter
    def ignore_public_acls(self, ignore_public_acls):
        r"""Sets the ignore_public_acls of this SetBpaRequestBody.

        Whether to ignore the existing ACL that allows public access to the bucket or objects in the bucket. If this parameter is set to true, the public access ACL of the bucket or objects in the bucket becomes invalid.

        :param ignore_public_acls: The ignore_public_acls of this SetBpaRequestBody.
        :type ignore_public_acls: bool
        """
        self._ignore_public_acls = ignore_public_acls

    @property
    def restrict_public_buckets(self):
        r"""Gets the restrict_public_buckets of this SetBpaRequestBody.

        Whether to restrict the existing public bucket policy. If this parameter is set to true, only the cloud service and bucket owner accounts are allowed to access the bucket.

        :return: The restrict_public_buckets of this SetBpaRequestBody.
        :rtype: bool
        """
        return self._restrict_public_buckets

    @restrict_public_buckets.setter
    def restrict_public_buckets(self, restrict_public_buckets):
        r"""Sets the restrict_public_buckets of this SetBpaRequestBody.

        Whether to restrict the existing public bucket policy. If this parameter is set to true, only the cloud service and bucket owner accounts are allowed to access the bucket.

        :param restrict_public_buckets: The restrict_public_buckets of this SetBpaRequestBody.
        :type restrict_public_buckets: bool
        """
        self._restrict_public_buckets = restrict_public_buckets

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
        if not isinstance(other, SetBpaRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
